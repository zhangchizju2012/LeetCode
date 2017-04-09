#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:30:01 2017

@author: zhangchi
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ''
        result = ''
        for i in s:
            if i != ' ':
                temp = i + temp
            else:
                result = result + ' '+ temp
                temp = ''
        result = result + ' '+ temp
        return result[1:]
        '''
        temp = s.split(' ')
        result = ''
        for item in temp:
            for i in range(len(item)-1,-1,-1):
                result += item[i]
            result += ' '
        return result[:-1]
        '''
s = Solution()
#print s.reverseWords("enuk$)g*)(mex%y*ocdafa)ev%konbr(ucvu*kjh$kyz*djrk)rniq##jbqtwhu*r&q#gsd#ivkni (xkpffov(frqu)!&sf&stbw)@s! eq&tj)vguf!y$sstm^! @mx%khlj$jpqs*uxwxvgu vjmlw^ubivqyyljta%q&$f@mcvc&(owvgyehq#qph*fak tqxtey kexylyiwh%!bxpcqo@zgg&tklpw%phs)cbo@(&^^wn w*xhpxa@d!!vwavwqchbfmpl&z@$kztz#nc%@!tv$htr!&d(wbj^tcfpu!z)!hyf^&sc!c)z%bgufbj#obhlykh ih$vxc*to#*wombce*eo)pqftfps^c(&kf%clklc f&$murkgdhnos$%ovvaqc&las%r%s*x^cpqvk&xlbmxejlsyt^(ck$ @)ks$i!dotdz)skwc&s^zk!ma!z@ymd%d)(flj^)va*tr^xnjgd!x b!al&bvewa#wtr^pov v$aie%x&&bx#@mnwrvu&^v$je(#se&y)x$wmgzmi!%eixawazf%*g$obyggoybw#ygjg**u(it@^b)@raa#ua(w*wxensgd u(a%qinf#wgoxt(q!&rz)ktpuqrjswqr^kispf*gzv#nkyg icd)xfhdpwwvm@i$%&ov(xkbe)igwajs@v)nepqtbjtk $dexm*bapttglgj$azwcaobdj&$ol#jnoq(f&twe@ulovnliefy%(%uncco%z#%%&w@xanjxdd")
print s.reverseWords("")
