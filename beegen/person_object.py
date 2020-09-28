# Person definition 

class Person(object):
    ''' Object that defines a person and his/her attributes.

    Attributes:
        unique_id: unique identifier for the person
        gender: (string) ['male', 'female', 'unknown']
        mother: (string) unique identifier to mother or 'unknown'
        father: (string) unique identifier to father or 'unknown'
        twin: (dictionary or None)
            None: if not a twin
            dictionary: {twin_id: (list of twin unique_ids),
                         twin_type: (list of twin types ['MZ', 'DZ'])}
        attibutes_dict: (dictionary or None) key: value pair of any attribute added to the person
    '''
    def __init__(self, unique_id, gender='unknown', mother='unknown', 
                father='unknown', twin=None, attributes_dict=None):
        ''' Constructor for person object, attributes dict gets added to class as object.'''
        self.unique_id = unique_id

        # Check Gender Status
        if gender.lower() == 'male':
            gender = 'Male'
        elif gender.lower() == 'female':
            gender = 'Female'
        else:
            gender = 'Unknown'
        self.gender = gender

        # Check Parental Status
        self.mother = 'Unknown' if mother.lower() == 'unknown' else mother
        self.father = 'Unknown' if father.lower() == 'unknown' else father

        # Validate twin status
        if twin is not None:
            if not isinstance(twin, dict):
                raise TypeError('Twin input must be a dictionary or None')

            if len(twin['twin_id']) != len(twin['twin_type']):
                raise ValueError('Twin ID and Twin Type must be the same length')
            
            for twin_type in twin['twin_type']:
                if twin_type not in ['MZ', 'DZ']:
                    raise ValueError('Twin type must be either MZ or DZ')
        self.twin = twin

        # Add extra attributes
        if isinstance(attributes_dict, dict):
            self.__dict__.update(attributes_dict)

