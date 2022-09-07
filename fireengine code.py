from typing import Iterable
import collections
import matplotlib.pyplot as plt
import numpy as np 
from itertools import chain

# 6.5... is actually 6.s...
# number.901 is actually number.c01
# 6.000 is actually 6.UAR and 6.999 is actually 6.UAT



course_bible = {}
total_majors = input("enter the total number of MIT majors you would like to compare (CURRENT LIMIT = 12): ")
disclaimer = print("the following MIT majors are available for comparison: 6-1, 6-1/8-flex, 6-2 old, 6-2 new, 6-3 old, 6-3 new, 6-4, 6-7, 6-14, 6-9, 11-6, 15-2")

while len(course_bible) < int(total_majors):
    course_num = input("Enter the Course/Major Number: ")
    
    programming_skills = [6.0001]
    math = [18.03]
    ee_foundation = [6.004, 6.002, 6.003] 
    ee_header = [6.014, 6.013, 6.012, 6.011, 6.036, 6.021, 6.640]
    aus2 = [18.404, 6.170, 6.172, 6.035, 6.818, 6.054, 6.053, 6.039, 6.808, 6.175, 6.101, 6.111, 6.115, 6.1151, 6.301, 6.061, 6.131, 6.1311, 6.701, 6.302, 6.207, 6.401, 6.419, 6.817, 6.800, 6.837, 6.807, 6.810, 6.023, 6.027, 6.025, 6.816, 6.905, 6.814, 6.812, 6.602, 6.215, 6.819, 6.815, 6.806, 6.047, 6.802, 6.580, 6.026, 6.5046, 6.5082, 6.5083]
    eecs_list = [18.600, 2.007, 6.0001, 6.0002, 6.009, 6.031, 6.170, 6.172, 6.035, 6.818, 6.042, 6.006, 6.046, 6.045, 6.053, 6.033, 6.808, 6.052, 6.004, 6.175, 6.002, 6.101, 6.111, 6.115, 6.1151, 6.301, 6.061, 6.014, 6.131, 6.1311, 6.013, 6.161, 6.051, 6.157, 6.012, 6.701, 6.152, 6.003, 6.011, 6.302, 6.207, 6.02, 6.041, 6.431, 6.419, 6.008, 6.036, 6.034, 6.804, 6.817, 6.141, 6.800, 6.837, 6.807, 6.810, 6.811, 6.185, 6.073, 6.805, 6.049, 6.021, 6.022, 6.023, 6.024, 6.027, 6.025, 6.129, 6.03, 6.816, 6.905, 6.814, 6.812, 6.602, 6.215, 6.819, 6.815, 6.806, 6.047, 6.802, 6.580, 6.026, 6.08, 6.943, 6.163, 6.01, 6.935, 6.901, 1.901, 10.901, 2.901, 20.901, 22.901, 3.901, 6.5047, 6.000, 6.999]
    dlab2 = [6.170, 6.172, 6.035, 6.808, 6.175, 6.101, 6.111, 6.115, 6.1151, 6.301, 6.321, 6.131, 6.1311, 6.161, 6.152, 6.302, 6.320, 6.141, 6.837, 6.807, 6.185, 6.073, 6.025, 6.129, 6.816, 6.819, 6.839, 6.806, 6.047, 6.026, 6.163, 6.5046]
    ii = [6.170, 6.172, 6.035, 6.818, 6.054, 6.808, 6.052, 6.111, 6.1151, 6.1311, 6.161, 6.419, 6.804, 6.141, 6.800, 6.807, 6.810, 6.811, 6.805, 6.129, 6.905, 6.819, 6.806, 6.047, 6.163, 6.5083, 6.000]
    prob = [18.05, 18.600, 6.042, 6.041, 6.008] 
    cim2 = [6.033, 6.101, 6.115, 6.1151, 6.131, 6.1311, 6.161, 6.152, 6.141, 6.800, 6.805, 6.025, 6.129, 6.819, 6.806, 6.163, 6.000, 6.999]

    ee_physics_foundation = [6.002, 6.003] 

    eecs_old_foundation = [6.009, 6.006, 6.004, 6.002, 6.003, 6.008]
    eecs_old_header = [6.031, 6.046, 6.045, 6.033, 6.014, 6.013, 6.012, 6.011, 6.036, 6.034, 6.021, 6.640]
    cs12 = [6.009, 6.031, 6.006, 6.046, 6.045, 6.033, 6.034]
    ee12 = [6.002, 6.014, 6.013, 6.012, 6.003, 6.011, 6.021, 6.640]
    eecs12 = [6.004, 6.008, 6.036]

    fundamental = [6.0001, 6.042, 6.006, 6.0004]
    eecs_new_math = [18.06, 6.041, 6.008, 18.05]
    systems_design = [6.004, 6.002, 6.302, 6.010]
    
    biomedical_systems = [6.020, 6.021, 6.022, 6.023, 6.025]
    communications_networks = [6.405, 6.033, 6.003, 6.011]
    devices_circuits_systems = [6.101, 6.300, 6.301, 6.111, 6.115, 6.131, 6.013, 6.012]
    electromagnetics_photonic_systems = [6.014, 6.013, 6.161, 6.602]
    embedded_systems = [6.808, 6.111, 6.115, 6.810]
    energy_systems = [6.061, 6.014, 6.131]
    hardware_design = [6.175, 6.111, 6.115, 6.374]
    hardware_software = [6.033, 18.404, 6.170, 6.172, 6.035, 6.818, 6.046, 6.045, 6.054, 6.053, 6.039, 6.808, 6.052, 6.810, 6.811, 6.185, 6.805, 6.827, 6.836, 6.816, 6.820, 6.822, 6.854, 6.856, 6.851, 6.852, 6.849, 6.850, 6.853, 6.847, 6.840, 6.841, 6.842, 6.845, 6.857, 6.875, 6.876, 6.858, 6.828, 6.829, 6.830, 6.814, 6.824, 6.826, 6.835, 6.859]
    nanoelectronics = [6.012, 6.015, 6.152]
    quantum_systems = [6.051, 6.157]
    systems_science = [6.003, 6.011, 6.207, 6.401, 6.036, 6.038, 6.141, 6.800, 6.215, 6.819]
    plab = [6.035, 6.808, 6.101, 6.111, 6.115, 6.131, 6.161, 6.152, 6.141, 6.807, 6.810, 6.185, 6.025]
    ee_track = list(chain(biomedical_systems, communications_networks, devices_circuits_systems, electromagnetics_photonic_systems, embedded_systems, energy_systems, hardware_design, hardware_software, nanoelectronics, quantum_systems, systems_science))
    
    discrete_math = [6.042]
    cs_old_foundation = [6.009, 6.006, 6.004]
    cs_old_header = [6.031, 6.045, 6.046, 6.033, 6.034, 6.036]

    cs_new_programming_skills = [6.0001, 6.0004]
    cs_new_math = [18.05, 18.06, 6.041, 6.008]
    cs_new_foundation = [6.009, 6.006, 6.004]
    cs_new_header = [6.031, 6.045, 6.046, 6.033]

    csee_architecture = [6.175, 6.111, 6.115, 6.823, 6.825, 6.812]
    computers_society = [6.052, 6.805, 6.859]
    human_computer_interaction = [6.170, 6.810, 6.811, 6.185, 6.835, 6.859]
    programming_principles_tools = [6.170, 6.172, 6.035, 6.818, 6.827, 6.836, 6.816, 6.820, 6.822]
    systems = [6.053, 6.039, 6.808, 6.857, 6.858, 6.828, 6.829, 6.830, 6.814, 6.824, 6.826]
    theory = [18.404, 6.046, 6.045, 6.054, 6.827, 6.854, 6.856, 6.851, 6.852, 6.849, 6.850, 6.853, 6.847, 6.840, 6.841, 6.842, 6.845, 6.875, 6.876]
    cs_track = list(chain(csee_architecture, computers_society, human_computer_interaction, programming_principles_tools, systems, theory))

    application = [18.404, 6.419, 6.141, 6.800, 6.905, 6.814, 6.819, 6.815, 6.806, 6.047, 6.802]
    centers = [6.046, 6.003, 6.302, 6.207, 6.401, 6.036, 6.404, 6.038, 6.804, 6.837, 6.805, 6.215, 18.404, 6.419, 6.141, 6.800, 6.905, 6.814, 6.819, 6.815, 6.806, 6.047, 6.802]
    ai_d_track = list(chain(application, centers))

    ai_math = [6.042, 18.06, 6.041, 6.008, 18.05]
    ai_foundation = [6.009, 6.006]
    data_centric = [6.401, 6.036]
    model_centric = [6.003, 6.038, 6.837]
    decision_centric = [6.302, 6.038, 6.215]
    computation_centric = [6.046, 6.837, 6.215]
    human_centric = [6.207, 6.404, 6.804, 6.805]
    application_cim = [6.141, 6.800, 6.819, 6.806]
    ai_d_aus = [18.404, 6.419, 6.905, 6.814, 6.815, 6.047, 6.802]
    serc = [6.036, 6.404, 6.805, 6.819, 6.806]

    cs_bio_intro = [6.0001, 6.0002, 6.031, 6.009]
    cs_bio_foundation = [6.006, 6.046]
    intro_lab = [6.129]
    compbio_elective = [6.049, 6.047, 6.802]
    biore_elective = [6.049]
    communication_intensive = [6.000, 6.999]

    cs_econ_math = [18.06, 6.041, 18.600, 6.042, 14.30]
    computation_algorithms = [6.0001, 6.009, 6.0002, 6.006, 6.046, 6.036]
    economics = [14.01, 14.03, 14.32, 14.05, 14.18, 14.33]
    probability_statistics = [6.207, 6.125, 15.053]
    econds = [14.20, 14.27, 14.36, 14.38, 14.41, 14.42, 14.43, 14.44, 14.64, 14.75, 14.76, 15.0201, 15.037, 15.780]
    econth = [14.04, 14.12, 14.13, 14.16, 14.19, 14.26, 14.54, 15.039, 6.207]
    econ_ci = [15.276, 6.000, 6.999]

    cs_urban_requirement = [6.0001, 6.0002, 6.042, 6.006, 6.009, 6.031, 6.008, 6.034, 6.036, 6.041, 6.805]
    cs_urban_electives = [6.803, 6.811, 6.815, 6.837, 6.170, 15.276, 6.805, 6.000]

    cs_cognition_requirement = [6.0001, 6.042, 18.03, 18.06, 6.008, 6.041]
    eecs_cognition_program = [6.036, 6.003, 6.034, 6.002, 6.006, 6.009]
    joint_electives = [6.027, 6.034, 6.141, 6.801, 6.803, 6.806, 6.819]
    cs_cognition_lab = [6.101, 6.111, 6.115, 6.129, 6.141, 6.161, 6.182]

    business_requirements = [15.076, 15.276, 6.0001, 6.0002, 15.312, 15.053, 15.069, 18.05, 14.30, 15.780, 6.036]
    business_restriced_electives = [15.0201, 15.0251, 15.0341, 15.037, 15.0621, 15.068, 15.0711, 15.093, 15.285, 15.450, 15.456, 15.458, 15.570, 15.669, 15.6731, 15.690, 15.7611, 15.762, 15.763, 15.772, 15.777, 15.8141, 15.819, 15.871, 15.8731, 15.874, 15.401, 15.417, 15.501, 15.9001, 1.022, 1.041, 6.034, 6.042, 6.4120, 14.12, 6.3260, 14.32, 18.06, 18.615, 6.3730]

    ee_major = list(chain(programming_skills, math, ee_foundation, ee_header, aus2, eecs_list, dlab2, ii, prob, cim2))
    ee_physics_major = list(chain(programming_skills, math, ee_physics_foundation, ee_header, aus2, eecs_list, dlab2, ii, prob, cim2))
    eecs_old_major = list(chain(programming_skills, math, eecs_old_foundation, eecs_old_header, aus2, eecs_list, dlab2, ii, prob, cim2, cs12, ee12, eecs12))
    eecs_new_major = list(chain(fundamental, eecs_new_math, systems_design, eecs_list, cim2, plab, ee_track))
    cs_old_major = list(chain(programming_skills, discrete_math, cs_old_foundation, cs_old_header, aus2, eecs_list, ii, cim2))
    cs_new_major = list(chain(cs_new_programming_skills, discrete_math, cs_new_math, cs_new_foundation, cs_new_header, ee_track, eecs_list, aus2, ii, cim2, ai_d_track, cs_track))
    ai_major = list(chain(programming_skills, ai_math, ai_foundation, data_centric, model_centric, decision_centric, computation_centric, human_centric, application_cim, cim2, ai_d_aus, eecs_list, serc))
    cs_bio_major = list(chain(cs_bio_intro, discrete_math, cs_bio_foundation, intro_lab, compbio_elective, biore_elective, communication_intensive))
    cs_econ_major = list(chain(cs_econ_math, computation_algorithms, economics, probability_statistics, econds, econth, econ_ci))
    cs_cognition_major = list(chain(cs_cognition_lab, cs_cognition_requirement, eecs_cognition_program, joint_electives, communication_intensive))
    cs_urban_major = list(chain(cs_urban_electives, cs_urban_requirement))
    business_analytics_major = list(chain(business_requirements, business_restriced_electives))
    
    course_bible_fill = {"6-1": ee_major, "6-1/8-flex": ee_physics_major, "6-2 old":  eecs_old_major, "6-2 new": eecs_new_major, "6-3 old":  cs_old_major, "6-3 new":  cs_new_major, "6-4": ai_major,"6-7": cs_bio_major, "6-14": cs_econ_major, "6-9": cs_cognition_major, "11-6": cs_urban_major, "15-2": business_analytics_major}
    
    if course_num not in course_bible: # check if key not in dict
        if course_num in course_bible_fill:
            course_bible[course_num] = course_bible_fill[course_num] # creates key and value
        else: 
            print("This course is not available for comparison. Please try a different major.")

def get_all_values(d):
    if isinstance(d, dict):
        for v in d.values():
            yield from get_all_values(v)
    elif isinstance(d, Iterable): # Iterable = list, set, etc
        for v in d:
            yield from get_all_values(v)
    else:
        yield d
list_all_classes = list(get_all_values(course_bible)) # creates one list of all the values

counter = collections.Counter(list_all_classes)
course_and_counter = counter.most_common() 
# print(course_and_counter) ... [(18.03, 2), (6.002, 1), (6.009, 1)]

xdata = []
ydata = []
for first, second in course_and_counter:
    x = str(first)
    xdata.append(x)
    y = second
    ydata.append(y)

fig = plt.figure(figsize = (50, 30))
plt.bar(xdata, ydata, color ='maroon', width = 0.4)
plt.yticks(np.arange(min(ydata), max(ydata)+1, 1.0))
plt.xlabel("Classes")
plt.xticks(fontsize=5, rotation=90)
plt.ylabel("Frequency")
plt.title("What Classes Should I Consider To Take?")
plt.show()