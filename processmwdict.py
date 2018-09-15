#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
processmwdict

Module for creating data structures from XML returned
from the Merriam-Webster Dictionary API

"""

# imports
import re
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

    def __init__(self):
        pass

    def dtbl(self, tag):
        """
        This is a dictionary that serves as a function dispatch for a given
        XML tag in the response from the MW Dictionary API
        """
        dt = {
            'cx'         : self.parse_cog_cross_entry,
            'date'       : self.parse_date,
            'def'        : self.parse_definition,
            'dro'        : self.parse_def_runon,
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
            'hw'         : self.parse_head_word,
            'in'         : self.parse_inflection,
            'lb'         : self.parse_label,
            'pl'         : self.parse_paragraph_label,
            'pr'         : self.parse_pronunciation,
            'pt'         : self.parse_paragraph_text,
            'sa'         : self.parse_synonym_see_additional,
            'sd'         : self.parse_sense_divider,
            'set'        : self.parse_sense_specific_etymology,
            'sin'        : self.parse_sense_specific_inflection,
            'slb'        : self.parse_sense_specific_label,
            'sn'         : self.parse_sense_number,
            'sound'      : self.parse_sound,
            'sp'         : self.parse_sense_specific_pronunciation,
            'ss'         : self.parse_synonym_see_cross_ref,
            'ssl'        : self.parse_sense_subject_label,
            'subj'       : self.parse_subject,
            'svr'        : self.parse_sense_variant,
            'uro'        : self.parse_undef_runon,
            'us'         : self.parse_usage,
            'vr'         : self.parse_variant,
            'vt'         : self.parse_verb_divider,
            'wav'        : self.parse_wavefile_name,
            'wpr'        : self.parse_wavefile_pronunciation,
        }

        print("dtbl : ", tag)

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

        return m1.group(1), text[m1.end():m2.start()], m2.group(1), \
            text[m2.end():]


    def parse_cog_cross_entry(self, text=None):
        """
        """
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['cl', 'ct', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('cx', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_date(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('date', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_defining_text(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['ca', 'dx', 'math', 'sx', 'un', 'vi']

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_definition(self, text=None):
#        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['date', 'dt', 'sd', 'sin', 'sn', 'ssl', 'us', 'vt']

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('def', text)

        # TODO: parse any tags inside of body
        
        while len(body) > 0:
            next_tag = self.peek_tag(body.lstrip().rstrip())
            
            if len(next_tag) == 0:
                break
            
            print('parse_definition - peek_tag: ', next_tag)
            
            open_tag, body, close_tag, remnant = \
                self.parse_tag(next_tag, text)
           

        return (open_tag, body, close_tag, remnant)




    def parse_def_runon(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['def', 'drp', 'et', 'vr']

        open_tag, body, close_tag, remnant = \
            self.parse_tag('dro', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_directional_cross_ref(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_directional_cross_ref_definition(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx_def', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_directional_cross_ref_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxt', 'it', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('dx_ety', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_directional_cross_ref_number(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('dxn', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_directional_cross_ref_target(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['dxn', 'inf', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('dxt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

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
                
                print('parse_entry - peek_tag: ', next_tag)

                a, b, c, entry_body = \
                    self.dtbl(self.peek_tag(entry_body.lstrip().rstrip())) \
                    (entry_body.lstrip().rstrip())

        return (open_entry_tag, entry_text, close_entry_tag, remnant)



    def parse_entry_list(self, text=None):

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
            
            print('parse_entry_list - peek_tag: ', 
                  self.peek_tag(remnant.lstrip().rstrip()))

            open_entry_tag, entry_body, close_entry_tag, remnant = \
                self.dtbl(self.peek_tag(remnant.lstrip().rstrip())) \
                (remnant.lstrip().rstrip())

            iter_ += 1

        return(open_entry_list_tag, entry_list_body, close_entry_list_tag, \
               remnant)

    def parse_entry_word(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('ew', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['it', 'ma', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('et', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_functional_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('fl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_head_word(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('hw', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_inflection(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['if', 'il', 'pr', ]

        open_tag, body, close_tag, remnant = \
            self.parse_tag('in', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []

        open_tag, body, close_tag, remnant = \
            self.parse_tag('lb', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_paragraph_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('pl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_paragraph_text(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('pt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('pr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_divider(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['snp', ]

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sd', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_sense_number(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['snp', ]

#        print('parse_sense_number: text: ', text)

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sn', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_specific_etymology(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['it', 'ma', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('set', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_specific_inflection(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['if', 'il', 'pr', 'spl',  ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('sin', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_specific_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('slb', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_specific_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('sp', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_sense_subject_label(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('ssl', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_sense_variant(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vl', 'va', 'pr', 'vpl', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('svr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_sound(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['wav', 'wpr']



        # TODO: parse any tags inside of body

        if (text is None or len(text) == 0):
            return None

        open_tag, body, close_tag, remnant = \
            self.parse_tag('sound', text)

        remnant = body

        while len((remnant.lstrip()).rstrip()) > 0:

            # now we have the tags enclosed in <entry_list> in the body.
            # we parse that for each <entry> tag.

            open_tag, body, close_tag, remnant = \
                self.dtbl(self.peek_tag(remnant))(remnant)

        return (open_tag, body, close_tag, remnant)

    def parse_subject(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('subj', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_synonym_see_cross_ref(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('ss', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)


    def parse_synonym_see_additional(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('sa', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_undef_runon(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['fl', 'in', 'lb', 'pr', 'sl', 'ure', 'uro', 'vr']

        open_tag, body, close_tag, remnant = \
            self.parse_tag('uro', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_usage(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('us', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_variant(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['va', 'vl', 'pr', 'sound', ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('vr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_verb_divider(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vi',  ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('vt', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_wavefile_name(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = []


        open_tag, body, close_tag, remnant = \
            self.parse_tag('wav', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

    def parse_wavefile_pronunciation(self, text=None):
        open_tag = None
        body = None
        close_tag = None
        remnant = None
        tag_list = ['vi',  ]


        open_tag, body, close_tag, remnant = \
            self.parse_tag('wpr', text)

        # TODO: parse any tags inside of body

        return (open_tag, body, close_tag, remnant)

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


#t_open, body, t_close, remnant = dp.parse_tag('entry_list', doc1)

DP.parse_entry_list(DOC1)
