
'''
    Contains Various text utility functions
'''
import re


def clean_text(text):
    '''
        Clean Text. Remove all special characters from text.
    '''
    cleaned_text = re.sub("[^a-zA-Z0-9]", " ", text)
    cleaned_text = re.sub(" +", " ", cleaned_text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text


def flatten_dictionary(input):
    '''
        @Input : An array of dictionaries
        @Output : Flatten array with one combined text field for each element.

        e.g: input = [{"a":"a1","b":"b1"}, {"a":"a2","b":"b2"}]
            output = ["a1 b1", "a2 b2"]
    '''

    res = []
    for d in input:
        res.append(" ".join([str(value) for value in d.values()]))
    return res
