# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:29:17 2025

@author: pc city
"""
#Kamran_Rostami_FanvariCo_Final_procet

class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):

        self.topic=topic
        
        self.topic_list=self.topic.split('/')        
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.port=port
        self.mqtt_broker=mqtt_broker 
        self.status='off'
        self.speed=0

        #self.connect_mqtt()
        #self.setup_gpio()

        
    def connect_mqtt(self):
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        print(f'{self.name} connected to mqtt')
        
        
    def setup_gpio(self):
        if self.device_tye=='lights':
            GPIO.setup(17,GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type=='doors': 
            GPIO.setup(27,GPIO.OUT)
            print(f'{self.name} connected to gpio')
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            if self.speed>0:
                GPIO.setup(18, GPIO.OUT)  # For fan speed, if using PWM
                #self.pwm = GPIO.PWM(18, 100)  # PWM frequency 100Hz
                #self.pwm.start(0)
                print(f'{self.name} connected to gpio')
                
                
                
            

    def turn_on(self):
        self.status='on'
        print(f'{self.name} is turned on')
        #self.send_command('TURN_ON') #ramzie k toye MQTT
        if self.device_type=='lights':
            pass
            #GPIO.output(17, GPIO.HIGH)
            
        elif self.device_type=='doors':
            pass
            #GPIO.output(27, GPIO.HIGH)
            
        elif self.device_type=='fans':
            pass
            #GPIO.output(22, GPIO.HIGH)
            
            
    def set_speed(self,speed):
        
        if self.status=='off':
            print(f'{self.name} currently is off')
            return None
        
        else:
            self.speed=speed
            #self.send_command(f'SET_SPEED:{speed}')
    


    def turn_off(self):
        self.status='off'
        print(f'{self.name} is turned off')
        #self.send_command('TURN_OFF')
        if self.device_type=='lights':
            #GPIO.output(17, GPIO.LOW)
            pass
            
        elif self.device_type=='doors':
            #GPIO.output(27, GPIO.LOW)
            pass
            
        elif self.device_type=='fans':
            #GPIO.output(22, GPIO.LOW)
            pass
            
        
    def get_status(self):
        return self.status
        
    
    def send_command(self,command):
        '''send a command via MQTT'''
        self.mqtt_client.publish(self.topic,command)
        print(f'command {command} send to topic {self.topic}')
        
        
    
a1=Device('home/living_room/lamps/lamp45')

a1.name

a1.group

a1.turn_on()

a1.get_status()


a1.turn_off()


a1.get_status()

a1=Device('home/living_room/lamps/lamps1')
a2=Device('home/living_room/lamps/rew')
a3=Device('home/living_room/lamps/lamtsrsp45')
a4=Device('home/living_room/lamps/lamp45')
a5=Device('home/living_room/lamps/lamp45')
a6=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')

class AdminPanel:

    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        ''' give me the name for one section of your house'''
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created')
            #logg mimone
        else:
            print('yout group name is duplicated name')
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            
           
        else:
            print(f'Group {group_name} does not exist')
        
        
    #dota function ro neveshtam ta inja bvrsm
    
    
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            
            
        else:
            print(f'Group {group_name} does not exist')
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                
                device_name=f"{device_type}{i}"
                
                topic=f'home/{group_name}/{device_type}/{device_name.lower()}'
            
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
            
            
        else:
            print(f'Group {group_name} does not exist')
            
            
            
            
        
    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name]
         
        else:
            print(f'Group {group_name} does not exist')
            return []
        
        

    def turn_on_all_in_group(self,group_name):
        devices=self.devices_ingroups(group_name)
        for device in devices:
            device.turn_one()
            #need a print
            
            
            
    def turn_off_all_in_group(self,group_name):
        
        ''' hameye cheragh haye yek goroh ra khamosh konad'''
        
        pass
        
    def trun_on_all(self):
        '''hameye device haro roshan kone'''
        pass
        
    def turn_off_all(self):
        '''hameye devcie haro khamosh kone'''
        pass
        
    def get_status_in_group(self,group_name):
        
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''
        pass
    def get_status_in_device_type(self,device_type):
        
        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''
        pass
    def create_sensor(self) :
    #bar asase clASS SENSOR argument bzarid
        pass
    
    
    
    def get_status_sensor_in_group(self,group_name):
        
        '''
        
        sensor haye yek goroh ro biad doone dooen status ro pas bde
        
        '''
        pass
        

        



a1=AdminPanel()

a1.create_group('living_room')
a1.create_multiple_devices('living_room','lamps',40)

a1.turn_on_all_in_group('living_room')

#check koni bbini roshan 

mygroups=a1.groups['living_room']

mygroups[1].name #lamps2'

mygroups[1].turn_on()

        
