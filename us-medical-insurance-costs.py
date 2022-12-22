#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[7]:


# Import csv library first:
import csv


# In[12]:


#We will now create lists for each category:
sexes = []
ages = []
bmis = []
num_of_children = []
regions = []
insurance_charges = []
smoker_or_nonsmoker = []


# In[16]:


#Now we load the list:

def load_list(csv_file, list_contents, category):
    with open('insurance.csv') as insurance_file:
        complete_dict = csv.DictReader(insurance_file)
        for row in complete_dict:
            list_contents.append(row[category])
        return list_contents
        


# In[20]:


#Use the load_list function on each of the seven lists:

load_list('insurance_csv', sexes, 'sex')
load_list('insurnace_csv', ages, 'age')
load_list('insurance_csv', bmis, 'bmi')
load_list('insurance.csv', num_of_children, 'children')
load_list('insurance.csv', regions, 'region')
load_list('insurance.csv', insurance_charges, 'charges')
load_list('insurance.csv', smoker_or_nonsmoker, 'smoker')


# In[35]:


# Arrange all of the data:
class PatientAttributes:
    def __init__(self, patient_sex, patient_age, patient_bmi, patient_children, patient_region, patient_charges, patient_smoker):
        self.patient_sexes = patient_sex
        self.patient_ages = patient_age
        self.patient_bmis = patient_bmi
        self.patient_children = patient_children
        self.patient_regions = patient_region
        self.patient_charges = patient_charges
        self.patient_smoker = patient_smoker
    
    def sex_analysis(self):
        # This will count each sex in the list:
        males = 0
        females = 0
        for sex in self.patient_sexes:
            if sex == 'male':
                males += 1
            elif sex == 'female':
                females += 1
        print('Number of males: ' + str(males))
        print('Number of females: ' + str(females))
        
    def age_analysis(self):
        # This will compute the average age in the entire list:
        total_age = 0
        for age in self.patient_ages:
            total_age += int(age)
        average_age = total_age / len(self.patient_ages)
        print('Average age: ' + str(average_age))
        
    def bmi_analysis(self):
        # This will compute the average bmi in the entire list:
        total_bmi = 0
        for bmi in self.patient_bmis:
            total_bmi += float(bmi)
        average_bmi = total_bmi / len(self.patient_bmis)
        print('Average BMI: ' + str(average_bmi))
        
    def children_analysis(self):
        # This will compute the average number of children in the entire list:
        total_children = 0
        for children in self.patient_children:
            total_children += int(children)
        average_children = total_children / len(self.patient_children)
        print('Average number of children: ' + str(average_children))
        
    def region_analysis(self):
        # This will compute the number of people from each region:
        northwest_count = 0
        northeast_count = 0
        southwest_count = 0
        southeast_count = 0
        for region in self.patient_regions:
            if region == 'northwest':
                northwest_count += 1
            elif region == 'northeast':
                northeast_count += 1
            elif region == 'southwest':
                southwest_count += 1
            elif region == 'southeast':
                southeast_count += 1
        print('There are ' + str(northwest_count) + ' people from the Northwest, and ' + str(northeast_count) + ' people from the Northeast.' + ' There are also ' + str(southwest_count) + ' people from the Southwest, and ' + str(southeast_count) + ' people from the Southeast.') 
                
    def charges_analysis(self):
        # This will compute the average charge for the entire list:
        total_charge = 0
        for charge in self.patient_charges:
            total_charge += float(charge)
        average_charge = float(total_charge) / len(self.patient_charges)
        print('Average insurance charge: ' + str(average_charge))
    
    def smoker_analysis(self):
        # This will compute the number of smokers and the number of non-smokers:
        smoker_count = 0
        nonsmoker_count = 0
        for status in self.patient_smoker:
            if status == 'yes':
              smoker_count += 1
            elif status == 'no':
              nonsmoker_count += 1
        print('There are ' + str(smoker_count) + ' smokers and ' + str(nonsmoker_count) + ' non-smokers.')
    
    def organize_dictionary(self):
        # This will create a dictionary with all of the attributes of the patients:
        self.full_dict = {}
        self.full_dict['age'] = self.patient_ages
        self.full_dict['sex'] = self.patient_sexes
        self.full_dict['bmi'] = self.patient_bmis
        self.full_dict['children'] = self.patient_children
        self.full_dict['regions'] = self.patient_regions
        self.full_dict['charges'] = self.patient_charges
        self.full_dict['smoker'] = self.patient_smoker
        


# In[38]:


# Testing the functions for analysis:

full_data = PatientAttributes(sexes, ages, bmis, num_of_children, regions, insurance_charges, smoker_or_nonsmoker)
full_data.sex_analysis()
full_data.bmi_analysis()
full_data.age_analysis()
full_data.children_analysis()
full_data.region_analysis()
full_data.smoker_analysis()


# In[ ]:


# Conclusions:
# The main influencer of medical insurance charges, based on the analysis of the data, was the variable of whether the patient smoked or not.
# This sample statistic is not biased AS LONG AS it was a random sample.

