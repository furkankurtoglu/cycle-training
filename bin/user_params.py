 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        div_row1 = Button(description='---Initial Parameters---', disabled=True, layout=divider_button_layout)

        param_name1 = Button(description='seeding_method', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.seeding_method = IntText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Transition Rates---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='r01', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.r01 = FloatText(
          value=0.01666,
          step=0.001,
          style=style, layout=widget_layout)

        param_name3 = Button(description='r01_fixed_duration', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.r01_fixed_duration = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name4 = Button(description='r12', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.r12 = FloatText(
          value=0.01666,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='r12_fixed_duration', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.r12_fixed_duration = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name6 = Button(description='r23', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.r23 = FloatText(
          value=0.01666,
          step=0.001,
          style=style, layout=widget_layout)

        param_name7 = Button(description='r23_fixed_duration', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.r23_fixed_duration = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name8 = Button(description='r30', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.r30 = FloatText(
          value=0.01666,
          step=0.001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='r30_fixed_duration', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.r30_fixed_duration = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Arresting phase link between G0/G1 and S---', disabled=True, layout=divider_button_layout)

        param_name10 = Button(description='r01_arrest', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.r01_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name11 = Button(description='oxygen_threshold', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.oxygen_threshold = FloatText(
          value=24,
          step=1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='oxygen_gradient', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.oxygen_gradient = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Arresting phase link between S and G2---', disabled=True, layout=divider_button_layout)

        param_name13 = Button(description='r12_arrest', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.r12_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name14 = Button(description='chemokine_threshold', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'lightgreen'

        self.chemokine_threshold = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        div_row5 = Button(description='---Arresting phase link between G2 an M---', disabled=True, layout=divider_button_layout)

        param_name15 = Button(description='r23_arrest', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'tan'

        self.r23_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name16 = Button(description='pressure_threshold', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'lightgreen'

        self.pressure_threshold = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        div_row6 = Button(description='---Arresting phase link between M an G0/G1 (division)---', disabled=True, layout=divider_button_layout)

        param_name17 = Button(description='r30_arrest', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'tan'

        self.r30_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name18 = Button(description='volume_threshold', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'lightgreen'

        self.volume_threshold = FloatText(
          value=2490.0,
          step=100,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='micrometer', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'lightgreen'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'
        units_button18 = Button(description='mM', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'lightgreen'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'

        desc_button2 = Button(description='For seeding one cell => 1, For tissue seeding => 2' , tooltip='For seeding one cell => 1, For tissue seeding => 2', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='transition rate between G0/G1 and S' , tooltip='transition rate between G0/G1 and S', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='True if transition rate (r01) are fixed duration.' , tooltip='True if transition rate (r01) are fixed duration.', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='transition rate between S and G2' , tooltip='transition rate between S and G2', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='True if transition rate (r12) are fixed duration.' , tooltip='True if transition rate (r12) are fixed duration.', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='transition rate between G2 and M' , tooltip='transition rate between G2 and M', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='True if transition rate (r23) are fixed duration.' , tooltip='True if transition rate (r23) are fixed duration.', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='transition rate between M and G0/G1' , tooltip='transition rate between M and G0/G1', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='True if transition rate (r30) are fixed duration.' , tooltip='True if transition rate (r30) are fixed duration.', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='if true and conditions were matched, it arrests phase link.' , tooltip='if true and conditions were matched, it arrests phase link.', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='environmental oxygen threshold for phase transition. If less than threshold, it stops' , tooltip='environmental oxygen threshold for phase transition. If less than threshold, it stops', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='True, if environment has oxygen gradient' , tooltip='True, if environment has oxygen gradient', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='arrest function according to chemokine level' , tooltip='arrest function according to chemokine level', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='environmental chemokine threshold for phase transition. If more, it stops' , tooltip='environmental chemokine threshold for phase transition. If more, it stops', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='arrest function according to pressure level' , tooltip='arrest function according to pressure level', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='cell pressure threshold to stall this phase transition. If more, it stops' , tooltip='cell pressure threshold to stall this phase transition. If more, it stops', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='arrest function according to cell volume' , tooltip='arrest function according to cell volume', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='target cell volume threshold. If less, it does not cycle.' , tooltip='target cell volume threshold. If less, it does not cycle.', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'

        row2 = [param_name1, self.seeding_method, units_button2, desc_button2] 
        row3 = [param_name2, self.r01, units_button4, desc_button3] 
        row4 = [param_name3, self.r01_fixed_duration, units_button5, desc_button4] 
        row5 = [param_name4, self.r12, units_button6, desc_button5] 
        row6 = [param_name5, self.r12_fixed_duration, units_button7, desc_button6] 
        row7 = [param_name6, self.r23, units_button8, desc_button7] 
        row8 = [param_name7, self.r23_fixed_duration, units_button9, desc_button8] 
        row9 = [param_name8, self.r30, units_button10, desc_button9] 
        row10 = [param_name9, self.r30_fixed_duration, units_button11, desc_button10] 
        row11 = [param_name10, self.r01_arrest, units_button13, desc_button11] 
        row12 = [param_name11, self.oxygen_threshold, units_button14, desc_button12] 
        row13 = [param_name12, self.oxygen_gradient, units_button15, desc_button13] 
        row14 = [param_name13, self.r12_arrest, units_button17, desc_button14] 
        row15 = [param_name14, self.chemokine_threshold, units_button18, desc_button15] 
        row16 = [param_name15, self.r23_arrest, units_button20, desc_button16] 
        row17 = [param_name16, self.pressure_threshold, units_button21, desc_button17] 
        row18 = [param_name17, self.r30_arrest, units_button23, desc_button18] 
        row19 = [param_name18, self.volume_threshold, units_button24, desc_button19] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)

        self.tab = VBox([
          div_row1,
          box2,
          div_row2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          div_row3,
          box11,
          box12,
          box13,
          div_row4,
          box14,
          box15,
          div_row5,
          box16,
          box17,
          div_row6,
          box18,
          box19,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.seeding_method.value = int(uep.find('.//seeding_method').text)
        self.r01.value = float(uep.find('.//r01').text)
        self.r01_fixed_duration.value = ('true' == (uep.find('.//r01_fixed_duration').text.lower()) )
        self.r12.value = float(uep.find('.//r12').text)
        self.r12_fixed_duration.value = ('true' == (uep.find('.//r12_fixed_duration').text.lower()) )
        self.r23.value = float(uep.find('.//r23').text)
        self.r23_fixed_duration.value = ('true' == (uep.find('.//r23_fixed_duration').text.lower()) )
        self.r30.value = float(uep.find('.//r30').text)
        self.r30_fixed_duration.value = ('true' == (uep.find('.//r30_fixed_duration').text.lower()) )
        self.r01_arrest.value = ('true' == (uep.find('.//r01_arrest').text.lower()) )
        self.oxygen_threshold.value = float(uep.find('.//oxygen_threshold').text)
        self.oxygen_gradient.value = ('true' == (uep.find('.//oxygen_gradient').text.lower()) )
        self.r12_arrest.value = ('true' == (uep.find('.//r12_arrest').text.lower()) )
        self.chemokine_threshold.value = float(uep.find('.//chemokine_threshold').text)
        self.r23_arrest.value = ('true' == (uep.find('.//r23_arrest').text.lower()) )
        self.pressure_threshold.value = float(uep.find('.//pressure_threshold').text)
        self.r30_arrest.value = ('true' == (uep.find('.//r30_arrest').text.lower()) )
        self.volume_threshold.value = float(uep.find('.//volume_threshold').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//seeding_method').text = str(self.seeding_method.value)
        uep.find('.//r01').text = str(self.r01.value)
        uep.find('.//r01_fixed_duration').text = str(self.r01_fixed_duration.value)
        uep.find('.//r12').text = str(self.r12.value)
        uep.find('.//r12_fixed_duration').text = str(self.r12_fixed_duration.value)
        uep.find('.//r23').text = str(self.r23.value)
        uep.find('.//r23_fixed_duration').text = str(self.r23_fixed_duration.value)
        uep.find('.//r30').text = str(self.r30.value)
        uep.find('.//r30_fixed_duration').text = str(self.r30_fixed_duration.value)
        uep.find('.//r01_arrest').text = str(self.r01_arrest.value)
        uep.find('.//oxygen_threshold').text = str(self.oxygen_threshold.value)
        uep.find('.//oxygen_gradient').text = str(self.oxygen_gradient.value)
        uep.find('.//r12_arrest').text = str(self.r12_arrest.value)
        uep.find('.//chemokine_threshold').text = str(self.chemokine_threshold.value)
        uep.find('.//r23_arrest').text = str(self.r23_arrest.value)
        uep.find('.//pressure_threshold').text = str(self.pressure_threshold.value)
        uep.find('.//r30_arrest').text = str(self.r30_arrest.value)
        uep.find('.//volume_threshold').text = str(self.volume_threshold.value)
