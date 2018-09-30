#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
processmwdict

Module for creating data structures from XML returned
from the Merriam-Webster Dictionary API

"""

# imports
import inspect
import os
import re
from stat import *
import uuid


#------------------------------------------------------------------------------

class MWSourceDoc:
    """
    TODO:
    """
    docRefId = ""
    contents = None

    def __init__(self, doc=""):
        self.docRefId = uuid.uuid4()
        self.sourceDoc = doc



#------------------------------------------------------------------------------

class MWDictProcessor:
    """
    class to process XML entries from the Merriam-Webster Dictionary API
    """
    # class member variables
    sourceDoc = None
    def_ = {}
    iter_ = 0
    cur_sense = None
    cur_subsense = None

    def __init__(self):
        pass

    def dtbl(self, tag):
        """
        This is a dictionary that serves as a function dispatch for a given
        XML tag in the response from the MW Dictionary API
        """
        dt = {
            'ahw'        : self.parse_alt_headword,
            'art'        : self.parse_art,
            'bold'       : self.parse_bold,
            'ca'         : self.parse_called_also,
            'cap'        : self.parse_cap,
            'cat'        : self.parse_called_also_target,
            'cx'         : self.parse_cog_cross_entry,
            'd'          : self.parse_d,
            'date'       : self.parse_date,
            'def'        : self.parse_definition,
            'dro'        : self.parse_def_runon,
            'drp'        : self.parse_def_runon_phrase,
            'dt'         : self.parse_defining_text,
            'dx'         : self.parse_directional_cross_ref,
            'dxn'        : self.parse_directional_cross_ref_number,
            'dxt'        : self.parse_directional_cross_ref_target,
            'dx_def'     : self.parse_directional_cross_ref_definition,
            'dx_ety'     : self.parse_directional_cross_ref_etymology,
            'entry_list' : self.parse_entry_list,
            'entry'      : self.parse_entry,
            'et'         : self.parse_etymology,
            'ew'         : self.parse_entry_word,
            'fl'         : self.parse_functional_label,
            'formula'    : self.parse_formula,
            'fw'         : self.parse_featured_word,
            'frac'       : self.parse_frac,
            'g'          : self.parse_g,
            'grp'        : self.parse_group,
            'hw'         : self.parse_head_word,
            'in'         : self.parse_inflection,
            'inf'        : self.parse_inferior_subscript,
            'it'         : self.parse_italicized_text,
            'lb'         : self.parse_label,
            'list'       : self.parse_list,
            'math'       : self.parse_math,
            'note'       : self.parse_note,
            'pl'         : self.parse_paragraph_label,
            'pr'         : self.parse_pronunciation,
            'pt'         : self.parse_paragraph_text,
            'ri'         : self.parse_ri,
            'rie'        : self.parse_rie,
            'sa'         : self.parse_synonym_see_additional,
            'sc'         : self.parse_small_caps,
            'sd'         : self.parse_sense_divider,
            'set'        : self.parse_sense_specific_etymology,
            'sin'        : self.parse_sense_specific_inflection,
            'sl'         : self.parse_status_label,
            'slb'        : self.parse_sense_specific_label,
            'sn'         : self.parse_sense_number,
            'sound'      : self.parse_sound,
            'sp'         : self.parse_sense_specific_pronunciation,
            'ss'         : self.parse_synonym_see_cross_ref,
            'ssl'        : self.parse_sense_subject_label,
            'subj'       : self.parse_subject,
            'suggestion' : self.parse_suggestion,
            'sup'        : self.parse_superior_superscript,
            'svr'        : self.parse_sense_variant,
            'sx'         : self.parse_synonymous_cross_ref,
            'sxn'        : self.parse_synonymous_cross_ref_sense_number,
            'table'      : self.parse_table,
            'un'         : self.parse_usage_note,
            'uro'        : self.parse_undef_runon,
            'us'         : self.parse_usage,
            'vi'         : self.parse_verbal_illustration,
            'vr'         : self.parse_variant,
            'vt'         : self.parse_verb_divider,
            'wav'        : self.parse_wavefile_name,
            'wpr'        : self.parse_wavefile_pronunciation,
        }

        # print("dtbl : ", tag, ' invoked from: ', inspect.getouterframes(inspect.currentframe())[1][3])

        if tag in dt:
            return dt[tag]
        else:
            print('dtbl: NOT IMPLEMENTED')
            return None



    def parse_tag(self, tag=None, text=None):
        """
        parse_tag - returns the contents of the XML tag provided
        params:
            tag - the XML tag to processs
            text - the XML docment to process
        returns:
            open_tag - the opening XML tag and any attributes
            body - the text inside of the XML tag start/end
            end_tag - the closing XML tag and any attributes
            remnant - leftover text after close tag
        """

        startTag = r'(<' +tag+' *[^>]*>)(?:[\s]*)'
        endTag = r'(</'+tag+' *[^>]*>)(?:[\s]*)'

        m1 = re.search(startTag, text)
        m2 = re.search(endTag, text)

        #  handle empty tags e.g. <sin/>
        if m2 is None: # this is most likely due to an empty tag
            return m1.group(1), '', m1.group(1), text[m1.end():]
        else:
            return m1.group(1), text[m1.end():m2.start()], m2.group(1), \
                text[m2.end():]

    def parse_alt_headword(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ahw', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_art(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('art', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_bold(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('bold', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_cap(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('cap', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)



    def parse_called_also(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ca', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_called_also_target(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('cat', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_cog_cross_entry(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['cl', 'ct', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('cx', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_d(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('d', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_date(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []
        
        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('date', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_defining_text(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['ca', 'dx', 'math', 'sx', 'un', 'vi']
        defdict = []

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dt', text)

        # when we get a <dt> tag, output the defining text along with the 
        # sense / subsense information
        
        # if sense is set but subsense is None:
        
        # if sense is set and subsense is not None:
        
        # if sense is None:

        ent = '(?:^[:]*)(.*)'

        m1 = re.search(ent, body)
        body = m1.group(1)

        
        defdict = {'sense' : self.cur_sense,
                   'subsense' : self.cur_subsense,
                   'def' : body }

#        print(defdict)
        
        # TODO: parse any tags inside of body
#----
# work in-process
        body_text = body.lstrip().rstrip()

        while len((body_text.lstrip()).rstrip()) > 0:

        # TODO: parse any tags inside of body

            next_tag = self.peek_tag(body_text.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break

            open_tag, body_text, close_tag, remnant2, js = \
                self.dtbl(next_tag)(body_text)
                
            body_text = remnant2
            if len(js) > 0:
                
                if next_tag == 'vi':
                    if 'vi' not in defdict:
                        defdict['vi'] = []
                    defdict['vi'].append(js)
                
#---

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_definition(self, text=None):
#        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['date', 'dt', 'sd', 'sin', 'sn', 'ssl', 'us', 'vt']
        defdict = []

        if (text is None or len(text) == 0):
            return None

        # When we encounter a new <def> tag, go ahead and reset the sense
        # variables
        self.sense = None
        self.subsense = None
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('def', text)

        # TODO: parse any tags inside of body
        # A <def> for an entry may have multiple <vt> tags if the pos of
        # the word is a verb.  Each of these <vt> tags will identify the
        # type of verb and will restart any previous sense numbering scheme.
        #
        # A <sn> tag may precede the <dt> tag if there are multiple senses
        # for that entry.  A <sn> tag may use one of the following schemes:
        #
        #   <sn>[1-n]</sn> - in this case, this is stand-alone sense number
        #       and will be associated with a single <dt>.
        #
        #   <sn>[1-n] [a-z]</sn> - in this case, this is the start of a new
        #       sense number with sub-senses.  Each sub-sense will have its
        #       own <dt> tag.
        #
        #   <sn>[a-z]</sn> - in this case, this is an additional sub-sense
        #       associated with the previous sense number.  It will have its
        #       own <dt> tag and should be associated with the prior top-level
        #       sense number.
        
        # this regex will parse any valid <sn> format and enable return via
        # the match.groupdict() function of the form
        # {'sense_no' : [0-9], 'subsense_no' : [a-z]'}
        
        sn_regex = '(?P<sense_no>[0-9]*)(?:[ ]*)(?P<subsense_no>[a-z]*)'
        
        self.cur_sense = None
        self.cur_subsense = None
        
        body_text = body.lstrip().rstrip()

        while len((body_text.lstrip()).rstrip()) > 0:

        # TODO: parse any tags inside of body

            next_tag = self.peek_tag(body_text.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break

            open_tag, body_text, close_tag, remnant2, js = \
                self.dtbl(next_tag)(body_text)
                
            body_text = remnant2
            if len(js) > 0:
                defdict.append(js)
                
        defdict = {'defs':defdict}

        return (open_tag, body, close_tag, remnant.lstrip().rstrip(), defdict)




    def parse_def_runon(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['def', 'drp', 'et', 'vr']
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('dro', text)

        body_text = body.lstrip().rstrip()

        while len((body_text.lstrip()).rstrip()) > 0:

        # TODO: parse any tags inside of body

            next_tag = self.peek_tag(body_text.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break

            open_tag, body_text, close_tag, remnant2, js = \
                self.dtbl(next_tag)(body_text)
                
            body_text = remnant2        

        return (open_tag, body, close_tag, remnant.lstrip().rstrip(), defdict)

    def parse_def_runon_phrase(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('drp', text)

        body_text = body.lstrip().rstrip()

        while len((body_text.lstrip()).rstrip()) > 0:

        # TODO: parse any tags inside of body
        
            next_tag = self.peek_tag(body_text.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break
                        

            open_tag, body_text, close_tag, remnant2, js = \
                self.dtbl(next_tag)(body_text)
                
            body_text = remnant2        

        return (open_tag, body, close_tag, remnant.lstrip().rstrip(), defdict)
    
    def parse_directional_cross_ref(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_directional_cross_ref_definition(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx_def', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_directional_cross_ref_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx_ety', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_directional_cross_ref_number(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dxn', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_directional_cross_ref_target(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxn', 'inf', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dxt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_entry(self, text=None):
        """
        For each entry, we want to parse out the following tags:
            <ew>    - this is the entry word for this instance
            <hw>    - this is the head word for the entry
            <fl>    - this is the part of speech
            <def>   - this is the collection of definitions for this entry
            <dro>   - these are the defined multi-word run-on wordsets with def
            <uro>   - these are the undef. multi-word run-on sets w/o defs
            <pr>    - pronunciation
            <sound> - .wav file with pronunciation of word
        """

        open_entry_tag = None
        entry_body = None
        close_entry_tag = None
        remnant = None
        tag_list = ['ahw', 'def', 'dro', 'et', 'ew', 'fl', 'grp', 'hw', 'pl', 
                    'pr', 'pt', 'sound', 'subj', 'uro']
        defdict = []
        
        entry_text = text

        if text is not None:
            # this is processing the <entry> tag itself.  DO NOT make the
            # mistake (again) of calling the dispatch table with the 'entry'
            # tag; it over-recurses.

            open_entry_tag, entry_body, close_entry_tag, remnant = \
                 self.parse_tag('entry', text)

            entry_text = entry_body

            # At some point, I'm going to forget why I didn't just implement
            # parse_tag instead of implementing all of the specific functions
            # for each tag.  At the time that I wrote this, I had no good
            # way to embed the 'rules' of how to process each sublevel's
            # embedded tags.  I'm sure at some point in the future I'll put
            # some time into this and come up with some clever way to handle
            # this, but now is not that time. - Rob.

            
            while len(entry_body.lstrip().rstrip()) > 0:
                
                next_tag = self.peek_tag(entry_body.lstrip().rstrip())
                
                if len(next_tag) == 0:
                    break
                
                a, b, c, entry_body, js = \
                    self.dtbl(self.peek_tag(entry_body.lstrip().rstrip())) \
                    (entry_body.lstrip().rstrip())
                    
#                defdict.append(js)
                if len(js) > 0:
                    defdict.append(js)

        defdict = {'entry':defdict}
        
        return (open_entry_tag, entry_text, close_entry_tag, remnant, defdict)



    def parse_entry_list(self, text=None):
        defdict = []
        
        iter_ = 0

        tag_list = ['entry']

        if (text is None or len(text) == 0):
            return None

        open_entry_list_tag, entry_list_body, close_entry_list_tag, \
            remnant = self.parse_tag('entry_list', text)

        remnant = entry_list_body

        while len((remnant.lstrip()).rstrip()) > 0:

            # now we have the tags enclosed in <entry_list> in the body.
            # we parse that for each <entry> tag.
            next_tag = self.peek_tag(remnant.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break
            
#            print('parse_entry_list - peek_tag: ', 
#                  self.peek_tag(remnant.lstrip().rstrip()))

            open_entry_tag, entry_body, close_entry_tag, remnant, js = \
                self.dtbl(self.peek_tag(remnant.lstrip().rstrip())) \
                (remnant.lstrip().rstrip())
                
#            defdict.append(js)
            if len(js) > 0:
                defdict.append(js)
                    
            iter_ += 1

        return(open_entry_list_tag, entry_list_body, close_entry_list_tag, \
               remnant, defdict)

    def parse_entry_word(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('ew', text)

        # TODO: parse any tags inside of body
        
        defdict = {'ew':body}

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['it', 'ma', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('et', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_featured_word(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('fw', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_formula(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('formula', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_frac(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('frac', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_functional_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = ""
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('fl', text)

        # TODO: parse any tags inside of body
        
        defdict = {'fl':body}

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_g(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = ""

        open_tag, body, close_tag, remnant = \
            self.parse_tag('g', text)

        # TODO: parse any tags inside of body


        return (open_tag, body, close_tag, remnant, defdict)


    def parse_group(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = ""

        open_tag, body, close_tag, remnant = \
            self.parse_tag('grp', text)

        # TODO: parse any tags inside of body


        return (open_tag, body, close_tag, remnant, defdict)

    def parse_head_word(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('hw', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_inferior_subscript(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('inf', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_inflection(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['if', 'il', 'pr', ]
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('in', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_italicized_text(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['if', 'il', 'pr', ]
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('it', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)



    def parse_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('lb', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_list(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('list', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_math(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('math', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_note(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('note', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_paragraph_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('pl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_paragraph_text(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('pt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('pr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_ri(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ri', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_rie(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('rie', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_divider(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['snp', ]
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('sd', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_sense_number(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['snp', ]
        defdict = []

        next_tag = self.peek_tag(text.lstrip().rstrip())

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sn', text)


        sn_regex = '(?P<sense_no>[0-9]*)(?:[ ]*)(?P<subsense_no>[a-z]*)'


        #print('parse_sense_number - peek_tag: ', next_tag)

        open_tag, body, close_tag, remnant = \
            self.parse_tag(next_tag, text)

        if next_tag == 'sn':
            # parse the current <sn> tag
            m1 = re.search(sn_regex, body)

            mdict = m1.groupdict()

            if mdict['sense_no'] != '':
                if self.cur_sense != mdict['sense_no']:
                    self.cur_subsense = None
                    
                self.cur_sense = mdict['sense_no']
                
            if mdict['subsense_no'] != '':
                self.cur_subsense = mdict['subsense_no']
            else:
                self.cur_subsense = None
                
            #print('sn - sense: ', self.cur_sense, ' subsense: ',
            #      self.cur_subsense)
            
        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_specific_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['it', 'ma', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('set', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_specific_inflection(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['if', 'il', 'pr', 'spl',  ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sin', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_specific_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('slb', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_specific_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sp', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sense_subject_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ssl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_sense_variant(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vl', 'va', 'pr', 'vpl', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('svr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_small_caps(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sc', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_sound(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['wav', 'wpr']
        defdict = []


        # TODO: parse any tags inside of body

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sound', text)

        body_text = body.lstrip().rstrip()

        while len((body_text.lstrip()).rstrip()) > 0:

        # TODO: parse any tags inside of body

            next_tag = self.peek_tag(body_text.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break

            open_tag, body_text, close_tag, remnant2, js = \
                self.dtbl(next_tag)(body_text)
                
            body_text = remnant2        

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_status_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_subject(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('subj', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_suggestion(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('suggestion', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_superior_superscript(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sup', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_synonymous_cross_ref(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sx', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_synonymous_cross_ref_sense_number(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sxn', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_synonym_see_cross_ref(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ss', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_synonym_see_additional(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sa', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_table(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('table', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_undef_runon(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['fl', 'in', 'lb', 'pr', 'sl', 'ure', 'uro', 'vr']
        defdict = []
        
        open_tag, body, close_tag, remnant = \
            self.parse_tag('uro', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_usage(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('us', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)
    
    def parse_usage_note(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('un', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)
    

    def parse_variant(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['va', 'vl', 'pr', 'sound', ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('vr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_verb_divider(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vi',  ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('vt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)


    def parse_verbal_illustration(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('vi', text)

        # TODO: parse any tags inside of body
        
        body_text = body.lstrip().rstrip()

#        while len((body_text.lstrip()).rstrip()) > 0:
#
#        # TODO: parse any tags inside of body
#
#            next_tag = self.peek_tag(body_text.lstrip().rstrip())
#            
#            if len(next_tag) == 0:
#                break
#
#            open_tag, body_text, close_tag, remnant2, js = \
#                self.dtbl(next_tag)(body_text)
#                
#            body_text = remnant2        

        defdict = {'vi':body}
        
        return (open_tag, body, close_tag, remnant, defdict)

    def parse_wavefile_name(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('wav', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def parse_wavefile_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vi',  ]
        defdict = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('wpr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant, defdict)

    def peek_tag(self, text=None):
        startTag = r'(?:[<])([a-zA-Z0-9]*)( *[^>]*)(?:[>])(?:[\s]*)'

        m1 = re.search(startTag, text.lstrip().rstrip())

        if m1 is not None:
            return m1.group(1)
        else:
            return ''

    def process_xml(self, xml=None):

        if xml is None:
            return self.def_
        else:
            # first, save the source xml into a MWSourceDoc object for ref
            self.sourceDoc = MWSourceDoc(xml)
            # now, parse out each <entry> element inside of the <entry_list>
            self.dtbl(self.peek_tag(xml))()

# end class MWDictProcessor
#------------------------------------------------------------------------------


DOC1 = """<?xml version="1.0" encoding="utf-8" ?>
<entry_list version="1.0">
	<entry id="bat[1]"><ew>bat</ew><subj>SB-3a#SC-3b#SP-3c#SB-4#TX-5</subj><hw hindex="1">bat</hw><sound><wav>bat00001.wav</wav><wpr>!bat</wpr></sound><pr>ˈbat</pr><fl>noun</fl><et>Middle English, from Old English <it>batt</it></et><def><date>before 12th century</date> <sn>1</sn> <dt>:a stout solid stick :<sx>club</sx></dt> <sn>2</sn> <dt>:a sharp blow :<sx>stroke</sx></dt> <sn>3 a</sn> <dt>:a usually wooden implement used for hitting the ball in various games</dt> <sn>b</sn> <dt>:a paddle used in various games (as table tennis)</dt> <sn>c</sn> <dt>:the short whip used by a jockey</dt> <sn>4 a</sn> <dt>:<sx>batsman</sx> <sx>batter</sx> <vi>a right-handed <it>bat</it></vi></dt> <sn>b</sn> <dt>:a turn at batting <un>usually used in the phrase <it>at bat</it></un></dt> <sn>c</sn> <dt>:hitting ability <vi>we need his <it>bat</it> in the lineup</vi></dt> <sn>5</sn> <dt>:<sx>batt</sx></dt> <sn>6</sn> <ssl>British</ssl> <dt>:rate of speed :<sx>gait</sx></dt> <sn>7</sn> <dt>:<sx>binge</sx></dt></def><dro><drp>off one's own bat</drp> <def><ssl>chiefly British</ssl> <dt>:through one's own efforts</dt></def></dro><dro><drp>off the bat</drp> <def><dt>:without delay :<sx>immediately</sx> <vi>recognized him right <it>off the bat</it></vi></dt></def></dro></entry>
	<entry id="bat[2]"><ew>bat</ew><subj>SB-vt1#SB-vt2#SB-vi1</subj><hw hindex="2">bat</hw><fl>verb</fl><in><if>bat*ted</if></in><in><if>bat*ting</if></in><def><vt>transitive verb</vt><date>15th century</date> <sn>1</sn> <dt>:to strike or hit with or as if with a bat</dt> <sn>2 a</sn> <dt>:to advance (a base runner) by batting</dt> <sn>b</sn> <dt>:to have a batting average of</dt> <sn>3</sn> <dt>:to discuss at length :consider in detail</dt><vt>intransitive verb</vt> <sn>1 a</sn> <dt>:to strike or hit a ball with a bat</dt> <sn>b</sn> <dt>:to take one's turn at bat</dt> <sn>2</sn> <dt>:to wander aimlessly</dt></def></entry>
	<entry id="bat[3]"><ew>bat</ew><subj>ZM</subj><hw hindex="3">bat</hw><fl>noun</fl><et>probably alteration of Middle English <it>bakke,</it> of Scandinavian origin; akin to Old Swedish natt<it>bakka</it> bat</et><def><date>1580</date><dt>:any of a widely distributed order (Chiroptera) of nocturnal usually frugivorous or insectivorous flying mammals that have wings formed from four elongated digits of the forelimb covered by a cutaneous membrane and that have adequate visual capabilities but often rely on echolocation</dt></def></entry>
	<entry id="bat[4]"><ew>bat</ew><hw hindex="4">bat</hw><fl>verb</fl><in><if>bat*ted</if></in><in><if>bat*ting</if></in><et>probably alteration of <it>bate</it></et><def><vt>transitive verb</vt><date>circa 1838</date><dt>:to wink especially in surprise or emotion <vi>never <it>batted</it> an eye</vi></dt> <sd>also</sd> <dt>:<sx>flutter</sx> <vi><it>batted</it> his eyelashes</vi></dt></def></entry>
	<entry id="BAT"><ew>BAT</ew><subj>ED</subj><hw>BAT</hw><fl>abbreviation</fl><def><dt>bachelor of arts in teaching</dt></def></entry>
	<entry id="batt"><ew>batt</ew><subj>TX</subj><hw>batt</hw><sound><wav>batt0001.wav</wav><wpr>!bat</wpr></sound><pr>ˈbat</pr><fl>noun</fl><def><date>1836</date><dt>:<sx>batting <sxn>2</sxn></sx></dt> <sd>also</sd> <dt>:an often square piece of <fw>batting</fw></dt></def></entry>
	<entry id="bat-eared fox"><ew>bat-eared fox</ew><subj>ZM</subj><hw>bat–eared fox</hw><sound><wav>batea01w.wav</wav><wpr>!bat-+ird-!f@ks</wpr></sound><pr>ˈbat-ˌird-</pr><fl>noun</fl><def><date>1946</date><dt>:a large-eared yellowish-gray fox (<it>Otocyon megalotis</it>) that inhabits arid unforested areas of eastern and southern Africa</dt></def></entry>
	<entry id="bat girl"><ew>bat girl</ew><subj>SB</subj><hw>bat girl</hw><fl>noun</fl><def><date>1969</date><dt>:a girl or woman employed to look after the equipment (as bats) of a baseball team</dt></def></entry>
	<entry id="bat mitzvah[1]"><ew>bat mitzvah</ew><subj>RJ</subj><hw hindex="1">bat mitz*vah</hw><sound><wav>batmi01w.wav</wav><wpr>b@t-!mits-vu</wpr></sound><pr>bät-ˈmits-və</pr><vr><vl>also</vl> <va>bas mitz*vah</va> <sound><wav>basmi01w.wav</wav><wpr>b@s-!mits-vu</wpr></sound> <pr>bäs-</pr></vr><fl>noun</fl><lb>often capitalized B&amp;M</lb><et>Hebrew <it>bath mişwāh,</it> literally, daughter of the (divine) law</et><def><date>1938</date> <sn>1</sn> <dt>:a Jewish girl who at 12 or more years of age assumes religious responsibilities</dt> <sn>2</sn> <dt>:the initiatory ceremony recognizing a girl as a bat mitzvah</dt></def></entry>
	<entry id="bat mitzvah[2]"><ew>bat mitzvah</ew><subj>RJ</subj><hw hindex="2">bat mitzvah</hw><vr><vl>also</vl> <va>bas mitzvah</va> </vr><fl>verb</fl><in><if>bat mitz*vahed</if> <il>also</il> <if>bas mitz*vahed</if></in><in><if>bat mitz*vah*ing</if> <il>also</il> <if>bas mitz*vah*ing</if></in><def><vt>transitive verb</vt><date>1976</date><dt>:to administer the ceremony of bat mitzvah to</dt></def></entry>
</entry_list>"""

DP = MWDictProcessor()

PATH = './dict/10k'
for f in os.listdir(PATH):

    fqn = os.path.join(PATH, f)
    mode = os.stat(fqn).st_mode
    if S_ISREG(mode):
        # print('{} is a file'.format(f))

        with open(fqn, 'r') as f:
            doc = f.read()
            a,b,c,d,e = DP.parse_entry_list(doc)
            print(e)
    # else:
    #     print('{} is not a file'.format(f))




