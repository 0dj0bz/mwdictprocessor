#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:33:09 2018

@author: robabbott
"""
import re
import uuid


class MWSourceDoc:
    docRefId = ""
    contents = None
    
    def __init__(self, doc = ""):
        self.docRefId = uuid.uuid4()
        self.sourceDoc = doc
        return None
    


class MWDictProcessor:
    
    sourceDoc = None
    def_ = {}
    
    def __init__(self):
        pass


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
        """
        
#        if (tag is None or text is None or len(text)==0):
#            return None

        startTag = r'(<' +tag+' *[^>]*>)(?:[\s]*)'
        endTag   = r'(</'+tag+' *[^>]*>)(?:[\s]*)'
        
#        start1,end1 = re.search(startTag, text).span()
#        tag1 = re.search(startTag, text).group()
#        start2,end2 = re.search(endTag, text).span()
#        tag2= re.search(endTag, text).group()
#        print(11*'=')
#        print(re.search(endTag, text).group())
#        print(11*'=')
#        return text[start1:end1], text[end1:start2], text[start2:end2], text[end2:]

        m1 = re.search(startTag, text)
        m2 = re.search(endTag, text)

        print(11*'=')
        print(m1.group(1))
        print(m2.group(1))
        print(11*'=')
        return m1.group(1), text[m1.end():m2.start()], m2.group(1), text[m2.end():]

            

    def parse_entry(self, text=None):
#        if (text is None or len(text)==0):
#            return None, None, None
        
        open_entry_tag = None
        entry_body = None
        close_entry_tag = None
        remnant = None
        
        if (text is not None): 
            open_entry_tag, entry_body, close_entry_tag, remnant = \
                 self.parse_tag('entry', text)
                 
            print(11*'+')
            print(entry_body)
            print(11*'+')
 
        if (remnant is not None and len(remnant)>0): 
            print(self.parse_entry(remnant))
 
        return(open_entry_tag, entry_body, close_entry_tag)
   
            
    def parse_entry_list(self, text=None):
        if (text is None or len(text)==0):
            return None
        
        open_entry_list_tag, entry_list_body, close_entry_list_tag, \
            remnant = self.parse_tag('entry_list', text)
            # now we have the tags enclosed in <entry_list> in the body.
            # we parse that for each <entry> tag.
    
        self.parse_entry(entry_list_body)
    
        return(open_entry_list_tag, entry_list_body, close_entry_list_tag, \
               remnant)
        

    def parse_entry_word(self):
        pass
    
    
    def process_xml(self, xml=None):
        
        if xml is None:
            return self.def_

        else:
            
            # first, save the source xml into a MWSourceDoc object for ref
            self.sourceDoc = MWSourceDoc(xml)
            
            # now, parse out each <entry> element inside of the <entry_list>
            
            pass
    
    
    
doc1 = """<?xml version="1.0" encoding="utf-8" ?>
<entry_list version="1.0">
	<entry id="bat[1]"><ew>bat</ew><subj>SB-3a#SC-3b#SP-3c#SB-4#TX-5</subj><hw hindex="1">bat</hw><sound><wav>bat00001.wav</wav><wpr>!bat</wpr></sound><pr>ˈbat</pr><fl>noun</fl><et>Middle English, from Old English <it>batt</it></et><def><date>before 12th century</date> <sn>1</sn> <dt>:a stout solid stick :<sx>club</sx></dt> <sn>2</sn> <dt>:a sharp blow :<sx>stroke</sx></dt> <sn>3 a</sn> <dt>:a usually wooden implement used for hitting the ball in various games</dt>  <sn>b</sn> <dt>:a paddle used in various games (as table tennis)</dt>  <sn>c</sn> <dt>:the short whip used by a jockey</dt> <sn>4 a</sn> <dt>:<sx>batsman</sx> <sx>batter</sx> <vi>a right-handed <it>bat</it></vi></dt>  <sn>b</sn> <dt>:a turn at batting <un>usually used in the phrase <it>at bat</it></un></dt>  <sn>c</sn> <dt>:hitting ability <vi>we need his <it>bat</it> in the lineup</vi></dt> <sn>5</sn> <dt>:<sx>batt</sx></dt> <sn>6</sn> <ssl>British</ssl> <dt>:rate of speed :<sx>gait</sx></dt> <sn>7</sn> <dt>:<sx>binge</sx></dt></def><dro><drp>off one's own bat</drp> <def><ssl>chiefly British</ssl> <dt>:through one's own efforts</dt></def></dro><dro><drp>off the bat</drp> <def><dt>:without delay :<sx>immediately</sx> <vi>recognized him right <it>off the bat</it></vi></dt></def></dro></entry>
	<entry id="bat[2]"><ew>bat</ew><subj>SB-vt1#SB-vt2#SB-vi1</subj><hw hindex="2">bat</hw><fl>verb</fl><in><if>bat*ted</if></in><in><if>bat*ting</if></in><def><vt>transitive verb</vt><date>15th century</date> <sn>1</sn> <dt>:to strike or hit with or as if with a bat</dt> <sn>2 a</sn> <dt>:to advance (a base runner) by batting</dt>  <sn>b</sn> <dt>:to have a batting average of</dt> <sn>3</sn> <dt>:to discuss at length :consider in detail</dt><vt>intransitive verb</vt> <sn>1 a</sn> <dt>:to strike or hit a ball with a bat</dt>  <sn>b</sn> <dt>:to take one's turn at bat</dt> <sn>2</sn> <dt>:to wander aimlessly</dt></def></entry>
	<entry id="bat[3]"><ew>bat</ew><subj>ZM</subj><hw hindex="3">bat</hw><fl>noun</fl><et>probably alteration of Middle English <it>bakke,</it> of Scandinavian origin; akin to Old Swedish natt<it>bakka</it> bat</et><def><date>1580</date><dt>:any of a widely distributed order (Chiroptera) of nocturnal usually frugivorous or insectivorous flying mammals that have wings formed from four elongated digits of the forelimb covered by a cutaneous membrane and that have adequate visual capabilities but often rely on echolocation</dt></def></entry>
	<entry id="bat[4]"><ew>bat</ew><hw hindex="4">bat</hw><fl>verb</fl><in><if>bat*ted</if></in><in><if>bat*ting</if></in><et>probably alteration of <it>bate</it></et><def><vt>transitive verb</vt><date>circa 1838</date><dt>:to wink especially in surprise or emotion <vi>never <it>batted</it> an eye</vi></dt> <sd>also</sd> <dt>:<sx>flutter</sx> <vi><it>batted</it> his eyelashes</vi></dt></def></entry>
	<entry id="BAT"><ew>BAT</ew><subj>ED</subj><hw>BAT</hw><fl>abbreviation</fl><def><dt>bachelor of arts in teaching</dt></def></entry>
	<entry id="batt"><ew>batt</ew><subj>TX</subj><hw>batt</hw><sound><wav>batt0001.wav</wav><wpr>!bat</wpr></sound><pr>ˈbat</pr><fl>noun</fl><def><date>1836</date><dt>:<sx>batting <sxn>2</sxn></sx></dt> <sd>also</sd> <dt>:an often square piece of <fw>batting</fw></dt></def></entry>
	<entry id="bat-eared fox"><ew>bat-eared fox</ew><subj>ZM</subj><hw>bat–eared fox</hw><sound><wav>batea01w.wav</wav><wpr>!bat-+ird-!f@ks</wpr></sound><pr>ˈbat-ˌird-</pr><fl>noun</fl><def><date>1946</date><dt>:a large-eared yellowish-gray fox (<it>Otocyon megalotis</it>) that inhabits arid unforested areas of eastern and southern Africa</dt></def></entry>
	<entry id="bat girl"><ew>bat girl</ew><subj>SB</subj><hw>bat girl</hw><fl>noun</fl><def><date>1969</date><dt>:a girl or woman employed to look after the equipment (as bats) of a baseball team</dt></def></entry>
	<entry id="bat mitzvah[1]"><ew>bat mitzvah</ew><subj>RJ</subj><hw hindex="1">bat mitz*vah</hw><sound><wav>batmi01w.wav</wav><wpr>b@t-!mits-vu</wpr></sound><pr>bät-ˈmits-və</pr><vr><vl>also</vl> <va>bas mitz*vah</va> <sound><wav>basmi01w.wav</wav><wpr>b@s-!mits-vu</wpr></sound> <pr>bäs-</pr></vr><fl>noun</fl><lb>often capitalized B&amp;M</lb><et>Hebrew <it>bath mişwāh,</it> literally, daughter of the (divine) law</et><def><date>1938</date> <sn>1</sn> <dt>:a Jewish girl who at 12 or more years of age assumes religious responsibilities</dt> <sn>2</sn> <dt>:the initiatory ceremony recognizing a girl as a bat mitzvah</dt></def></entry>
	<entry id="bat mitzvah[2]"><ew>bat mitzvah</ew><subj>RJ</subj><hw hindex="2">bat mitzvah</hw><vr><vl>also</vl> <va>bas mitzvah</va> </vr><fl>verb</fl><in><if>bat mitz*vahed</if> <il>also</il> <if>bas mitz*vahed</if></in><in><if>bat mitz*vah*ing</if> <il>also</il> <if>bas mitz*vah*ing</if></in><def><vt>transitive verb</vt><date>1976</date><dt>:to administer the ceremony of bat mitzvah to</dt></def></entry>
</entry_list>"""

dp = MWDictProcessor()
t_open, body, t_close, remnant = dp.parse_tag('entry_list', doc1)
print(dp.parse_entry(body))
