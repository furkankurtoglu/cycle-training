/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

// declare cell definitions here 

Cell_Definition cycle_cell; 

void create_cell_types( void )
{
	// use the same random seed so that future experiments have the 
	// same initial histogram of oncoprotein, even if threading means 
	// that future division and other events are still not identical 
	// for all runs 
	
	SeedRandom( parameters.ints("random_seed") ); // or specify a seed here 
	
	// housekeeping 
	
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// Name the default cell type 
	
	cell_defaults.type = 0; 
	cell_defaults.name = "default cell"; 
	
	// set default cell cycle model 

	cell_defaults.functions.cycle_model = flow_cytometry_separated_cycle_model; 
	
	// set default_cell_functions; 
	
	cell_defaults.functions.update_phenotype = cycle_arrest_function; 
	
	// needed for a 2-D simulation: 
	
	/* grab code from heterogeneity */ 
	
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0;
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// make sure the defaults are self-consistent. 
	
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 

	// set the rate terms in the default phenotype 

	// first find index for a few key variables. 
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );
	int oxygen_substrate_index = microenvironment.find_density_index( "oxygen" ); 
    int chemokine_substrate_index = microenvironment.find_density_index( "chemokine" );

	int G0G1_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::G0G1_phase );
	int S_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::S_phase );
    int G2_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::G2_phase );
    int M_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::M_phase );    

	// initially no necrosis 
	cell_defaults.phenotype.death.rates[necrosis_model_index] = 0.0; 
    cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0; 

	// set oxygen uptake / secretion parameters for the default cell type 
	cell_defaults.phenotype.secretion.uptake_rates[oxygen_substrate_index] = 0.0; 
	cell_defaults.phenotype.secretion.secretion_rates[oxygen_substrate_index] = 0; 
	cell_defaults.phenotype.secretion.saturation_densities[oxygen_substrate_index] = 0.0; 
	
	// add custom data here, if any 
	

	// Now, let's define another cell type. 
	// It's best to just copy the default and modify it. 
	
	// make this cell type randomly motile, less adhesive, greater survival, 
	// and less proliferative 
	
	cycle_cell = cell_defaults; 
	cycle_cell.type = 1; 
	cycle_cell.name = "cycle cell"; 
	
	// make sure the new cell type has its own reference phenotype
	
	cycle_cell.parameters.pReference_live_phenotype = &( cycle_cell.phenotype ); 
	
	// enable random motility 
	cycle_cell.phenotype.motility.is_motile = false; 
	
	cycle_cell.phenotype.cycle.data.transition_rate(G0G1_index,S_index) = parameters.doubles( "r01" );
	cycle_cell.phenotype.cycle.data.transition_rate(S_index,G2_index) = parameters.doubles( "r12" );
	cycle_cell.phenotype.cycle.data.transition_rate(G2_index,M_index) = parameters.doubles( "r23" );
    cycle_cell.phenotype.cycle.data.transition_rate(M_index,G0G1_index) = parameters.doubles( "r30" );
    
    
    if (parameters.bools("r01_fixed_duration"))
    {
        cycle_cell.phenotype.cycle.model().phase_link(G0G1_index,S_index).fixed_duration = parameters.bools("r01_fixed_duration");
    }
    
    if (parameters.bools("r12_fixed_duration"))
    {
        cycle_cell.phenotype.cycle.model().phase_link(S_index,G2_index).fixed_duration = parameters.bools("r12_fixed_duration");
    }
    
    if (parameters.bools("r23_fixed_duration"))
    {
        cycle_cell.phenotype.cycle.model().phase_link(G2_index,M_index).fixed_duration = parameters.bools("r23_fixed_duration");
    }    
    
    if (parameters.bools("r23_fixed_duration"))
    {
        cycle_cell.phenotype.cycle.model().phase_link(M_index,G0G1_index).fixed_duration = parameters.bools("r30_fixed_duration");
    } 

    
    
    cycle_cell.phenotype.secretion.uptake_rates[chemokine_substrate_index] = 0.0; 
	cycle_cell.phenotype.secretion.secretion_rates[chemokine_substrate_index] = 0.01; 
	cycle_cell.phenotype.secretion.saturation_densities[chemokine_substrate_index] = 10.0;  
	
	return; 
}

void setup_microenvironment( void )
{

	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
	// initialize BioFVM 
	
	initialize_microenvironment(); 	
	
    
    if (parameters.bools("oxygen_gradient"))
    {
        double oxy = 40.0;  // IC
        double oxy_del = 10.0;
        
        double x;
        double xmin = -500.;
        
        int nregions = 4;
        double xdel = 1000./nregions;
        // 5 regions across x: [-500:-300:-100:100:300:500]
        std::cout << "setup_microenvironment: num voxels= " << microenvironment.number_of_voxels() << std::endl;
        for( int n=0; n < microenvironment.number_of_voxels(); n++ )
        {
            // x coordinate of the nth voxel's center
            x = microenvironment.mesh.voxels[n].center[0];
            for( int iregion=1; iregion <= nregions; iregion++ )
            {
                if (x < (xmin + iregion*xdel))
                {
                    microenvironment(n)[0] = oxy - (iregion-1)*oxy_del;
                    break;
                }
                // oxy -= iregion-5;
                // glu -= iregion-2;
            }
        }
    }
	return; 
}

void setup_tissue( void )
{
	// create some cells near the origin
	
	Cell* pCell;
    
    int seeding_method  = parameters.ints("seeding_method");
    
    double initial_tumor_radius =  0;
    if (seeding_method == 1)
    {
        initial_tumor_radius = 8.2;
    }
    else if (seeding_method == 2)
    {
        initial_tumor_radius = 150;
    }
    else
    {
        std::cout << "WARNING! The seeding method should be either 1 or 2" << std::endl;
        std::cout << "Seeding only one cell..." << std::endl;
        initial_tumor_radius = 8.2;
    }
  

    double cell_radius = cell_defaults.phenotype.geometry.radius; 
	double cell_spacing = 0.8 * 2.0 * cell_radius; 
	
	std::vector<std::vector<double>> positions = create_cell_circle_positions(cell_radius,initial_tumor_radius);

    std::cout << "Creating cells" << std::endl;
    
    for( int i=0; i < positions.size(); i++ )
    {
        pCell = create_cell(cycle_cell);
        pCell->assign_position( positions[i] );
    }
	
	return; 
}


void cycle_arrest_function( Cell* pCell, Phenotype& phenotype , double dt )
{

    int G0G1_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::G0G1_phase );
	int S_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::S_phase );
    int G2_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::G2_phase );
    int M_index = flow_cytometry_separated_cycle_model.find_phase_index( PhysiCell_constants::M_phase );   
    bool r01_bool = parameters.bools( "r01_arrest" );
    bool r12_bool = parameters.bools( "r12_arrest" );
    bool r23_bool = parameters.bools( "r23_arrest" );
    bool r30_bool = parameters.bools( "r30_arrest" );
    
    
    //std::cout << "Arresting" << r01_bool << r12_bool << r23_bool << std::endl;
    


	

    
    
    if (r01_bool == 1)
    {
        // oxygen arresting
        static int oxygen_i = get_default_microenvironment()->find_density_index( "oxygen" );
        double pO2 = (pCell->nearest_density_vector())[oxygen_i];
        static double oxy_thr = parameters.doubles( "oxygen_threshold" );
        if ( pO2 < oxy_thr)
        {
            phenotype.cycle.data.transition_rate(G0G1_index,S_index) = 0.0;
            //std::cout << "Arrested" << std::endl;
        }
        if ( pO2 > oxy_thr)
        {
            phenotype.cycle.data.transition_rate(G0G1_index,S_index) = parameters.doubles( "r01" );
        }
        
    }
    
    if (r12_bool == 1)
    {
        // chemokine arresting
        static int chemokine_i = get_default_microenvironment()->find_density_index( "chemokine" );
        double pLactate = (pCell->nearest_density_vector())[chemokine_i];
        static double chem_thr = parameters.doubles( "chemokine_threshold" );
        if ( pLactate > chem_thr)
        {
            phenotype.cycle.data.transition_rate(S_index,G2_index) = 0.0;
            //std::cout << "Arrested" << std::endl;
        }
        if ( pLactate < chem_thr)
        {
            phenotype.cycle.data.transition_rate(S_index,G2_index) = parameters.doubles( "r12" );
        }
    }



    if (r23_bool == 1)
    {
        // pressure arrest
        double cell_pressure = pCell->state.simple_pressure;
        static double pre_thr = parameters.doubles( "pressure_threshold" );
        if ( cell_pressure > pre_thr)
        {
            phenotype.cycle.data.transition_rate(G2_index,M_index) = 0.0;
            //std::cout << "Arrested" << std::endl;
        }
        if ( cell_pressure < pre_thr)
        {
            phenotype.cycle.data.transition_rate(G2_index,M_index) = parameters.doubles( "r23" );
            //std::cout << "Arrested" << std::endl;
        }
    }


    if (r30_bool == 1)
    {
        // volume arrest
        double volume = phenotype.volume.total;
        //std::cout << volume << std::endl;
        static double vol_thr = parameters.doubles( "volume_threshold" );
        if ( volume < vol_thr)
        {
            phenotype.cycle.data.transition_rate(M_index,G0G1_index) = 0.0;
            //std::cout << "Arrested" << std::endl;
        }
        if ( volume > vol_thr)
        {
            phenotype.cycle.data.transition_rate(G2_index,M_index) = parameters.doubles( "r30" );
            //std::cout << "Arrested" << std::endl;
        }
        
    }    
    

    
	return;
}


std::vector<std::string> my_coloring_function( Cell* pCell )
{
	// start with flow cytometry coloring 
	
	std::vector<std::string> output = false_cell_coloring_cytometry(pCell); 
    char szTempString [128];
	if( pCell->phenotype.death.dead == false && pCell->type == 1 )
	{
		if( pCell->phenotype.cycle.current_phase_index() == 0 )
        {
            sprintf( szTempString , "rgb(230,97,1)");
            output[0].assign( szTempString );
            output[2].assign( szTempString );
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 1 )
        {
            char szTempString [128];
            sprintf( szTempString , "rgb(253,184,99)");
            output[0].assign( szTempString );
            output[2].assign( szTempString );
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 2 )
        {
            sprintf( szTempString , "rgb(178,171,210)");
            output[0].assign( szTempString );
            output[2].assign( szTempString );
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 3 )
        {
            sprintf( szTempString , "rgb(94,60,153)");
            output[0].assign( szTempString );
            output[2].assign( szTempString );
        }
        

	}
	
	return output; 
}

 
/*  std::vector<std::string> my_coloring_function( Cell* pCell )
{
	// start with flow cytometry coloring 
	
	std::vector<std::string> output = false_cell_coloring_cytometry(pCell); 
		
	if( pCell->phenotype.death.dead == false && pCell->type == 1 )
	{
		if( pCell->phenotype.cycle.current_phase_index() == 0 )
        {
            output[0] = "red"; 
            output[2] = "red"; 
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 1 )
        {
            output[0] = "green"; 
            output[2] = "green"; 
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 2 )
        {
            output[0] = "cornflowerblue"; 
            output[2] = "cornflowerblue"; 
        }
        
        if( pCell->phenotype.cycle.current_phase_index() == 3 )
        {
            output[0] = "mediumblue"; 
            output[2] = "mediumblue"; 
        }
        

	}
	
	return output; 
} */

std::vector<std::vector<double>> create_cell_circle_positions(double cell_radius, double sphere_radius)
{
	std::vector<std::vector<double>> cells;
	int xc=0,yc=0,zc=0;
	double x_spacing= cell_radius*sqrt(3);
	double y_spacing= cell_radius*sqrt(3);

	std::vector<double> tempPoint(3,0.0);
	// std::vector<double> cylinder_center(3,0.0);
	
	for(double x=-sphere_radius;x<sphere_radius;x+=x_spacing, xc++)
	{
		for(double y=-sphere_radius;y<sphere_radius;y+=y_spacing, yc++)
		{
			tempPoint[1]=y + (xc%2) * cell_radius;
			tempPoint[0]=x;
			tempPoint[2]=0;
			if(sqrt(norm_squared(tempPoint))< sphere_radius)
			{ cells.push_back(tempPoint); }
		}
	}
	return cells;
}