#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:39:30 2017

@author: zhangchi
"""

class Solution(object):
    # two pointers, inspired by solution, faster
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        else:
            dict1 = {}
            dict2 = {}
            for item in s1:
                if item in dict1:
                    dict1[item] += 1
                else:
                    dict1[item] = 1
            for item in s2[:len1]:
                if item in dict2:
                    dict2[item] += 1
                else:
                    dict2[item] = 1
            if self.checkSame(dict1,dict2) == True:
                return True
            for i in range(0,len2-len1):
                dict2[s2[i]] -= 1
                if s2[i+len1] not in dict2:
                    dict2[s2[i+len1]] = 1
                else:
                    dict2[s2[i+len1]] += 1
                if self.checkSame(dict1,dict2) == True:
                    return True
            return False
                
                
    def checkSame(self,dict1,dict2):
        for item in dict1:
            if item not in dict2 or dict1[item] != dict2[item]:
                return False
        return True

#==============================================================================
# # dfs generate permutation, slow
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if len(s1) > len(s2):
#             return False
#         dict1 = {}
#         dict2 = {}
#         for item in s1:
#             if item in dict1:
#                 dict1[item] += 1
#             else:
#                 dict1[item] = 1
#         for item in s2:
#             if item in dict2:
#                 dict2[item] += 1
#             else:
#                 dict2[item] = 1
#         for item in dict1:
#             if item not in dict2 or dict1[item] > dict2[item]:
#                 return False
#         self.s2 = s2
#         self.s1 = s1
#         length = len(s1)
#         self.length = length
#         return self.helper([],"")
#         
#     def helper(self,stop,string):
#         # permutation, dfs
#         if len(stop) == self.length:
#             return True
#         else:
#             for item in range(self.length):
#                 if item not in stop:
#                     temp = string + self.s1[item]
#                     if temp in self.s2:
#                         if self.helper(stop+[item],temp) == True:
#                             return True
#             return False
#==============================================================================
                            
s = Solution()
#'hello','ooolleoooleh'
#a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
#b = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
#c = "jpdojwinknmyeorfdhpsysyealozhgbapagzjsivbxmcyijlbdafupblrawguoazuzcqupobxayrkpqxawytdsdznljnxulaugewrbjmkslsrllixpkuvorhnnhkzikovsajrbhjdybocvjloqiikidsnwcubhliajwwqkpqaugidhfxqfxrkluvadcdmekdhckszpojvwpiquazmaecaxxwsnswzxbctqeqhjsrgnjsjmaqbexexuwgfglixsthifevokdgexxkdmzaxrcilmthzemuomexwzipzivdyxqnvgzpjavonrkobmgkormdmfiwwalgdzwlngkrjmdwkknajqatghoddybqfkorhpmrkfcfwsaproaenfedvfendprnlpmuqklsqrsjuejyxulfuhdsyolthhhfhmxorojnjsvqyworupkdzhyqkzikvhltfsrhrecmyyddtinphjsmmbdtrouyifvsvvlamwhkffrrywdiawpvxwcwfkcunbjaelbcmdwczikkfelahowtbwqbdcjggnmknfhjdtusfjotsbjgtlnuonlxjlcwyqiffktonvtrkcogosfbcvcosktnvbeitxuqpexxejnklndzbtzlzeebwufoiwqqcoemnshcpovntjgidophekyntcsrwzvovwmostqudxgeaowehcmqmdrllovmmbgqhaxrqluizhhhslystwkhckjtosnomfvyibkasycxnnmvkbwkbhzeayezughsmqovogrnihjgetsdvhymjmnijzwvpasurcaybmyzfbqepjsdqwmkmomzkociaqtnkwiguylhwxrfamyxjvfxwonwblidvcsenvwigjjqdsnnydlgdhlsdtonvuapzaozkdtyiartimmpwgotnwpiwimbdunqfickerusbvrqwazvnwgdczvnqtigjmkjgsridfulxjekazzqkdynyuutyoffhntfbcruhrmnhhjyyzfszbaqykgnroepiovqqlhdtkizvpivukdutitwzhapvcyfghqvtjyyrdbctvdccoxjtsovdosbyqaiffumnrfokrbgvedxbcytvbcaeoviutdmxwfhxgchnusazcztitxgyjrkjdmajbndlemsnpjwzgvpitrfrjoxivhisgkzncmkewphusvaycteennpltuevohegzvafwxuebmovgkpwlgyoutsbbgxoxdzyisersgaqcnnjnjtjwufqscjzccudbkdcnmorpmraqapvirijlpretmezlrbdvnfixvmalzmgrhwpkhisaztpsgvlooqxezzscjrtnmmctoyinjermwrrmjlfbizryripnarkvnabdizzereczdnbkojpfmxhlfvlztmzpskwttzyusxaudprxpbpihorlipzpdiucpvrqlscmoipvdzsrowjrwmxzomtcxxehrmcaxmtifcvftywjkzgdsohvomcthhylzpijujfyysbientozyirurugevubxpdpbihrudvgdmhwyxuhyorvufffqzifwzszmfswhkesywfyozffzarrklnxppymoaslqctlfbtrykccmgmhrdacuelfrbflsjxhdagaevscxerljtxnwodtfioyxjoaxyhzjmttvflfhqvvcbwvmnulcsubtwngjvomqkqrjtntkzuclolcjmiypjilgvezphjqrjetqnaccrjmxydmmkbmuyxwotfynptdotuaxpxzgjulwgwfbprzolxablskvidnmnzcofemsodetsiubqrvtbkshuokkuomjezwbmtcjvapnlsmutehyfxaqjqlibfzitcfhuivmmclulnrwyknbymyfcwbgyxtavcaebvfwlkikylkrpcfappcamnjenpggoxcrpxdbqjqzrdvnfzxuxuaixbpiqmitzhefcgyhzayemxgrtdoiryqguiexsrysetobkqnfphdechsgoqvmdhurzhvflsbxsdjemmvlzpthrjizfcayxemztvszhhpfvvjgoejrjnmyvxstpejfmiukuocmrgvinqifpdcqvwfddoiyopbzverxwcqdyoqzeqcjcwmojbhcnrksebanfpdhhpiaguxracnxzttbjgruczuhwwjbmznzgdijyemrwcawodqftjtlyozqwwchxtlvlnjqwklmbzirfhaquiltdijijeglroopaagmyrkhqbnkhbxvguodmmszfoomhfvwjsnrmmzjuyxhotehlezyyiptzububvazwzziskqagtpthflchvvanpugjpeoipecmvgkocylsqduwbreeifhjdomajmnbwrmxuhvvjnfblyvtveqalkqlbxkxvmxfefvijptnpvhmgmotrvsxmarhkspdlybniuoxycahgisvnrlrukendhsxvvcqzinnbkryzwbnktsgfwxjklrcgvtrzvkqfbhctljoijsvxbnwiunrasctvuetwvzdulmlnxeivsvujihlmjroxntmgkecjkimcsvfesfeursbuchaexgpyqakllumehlfdkuzbnulwfdacxjalozmrneqtjvdpgkcwnrkuhhqbnpedmysjqcrdqaawiwcucuzlbkwozlgrgcroyebklrwzkqicuqezkswayknmcytcsrtkxkfwxmimpolrqzjwfdzmlkpinifykobpvqlzqrcliorfqygytfgpdociwflhwpuuumrwnhrkpnteqacxejyulkccgxtnsfhuuahifvsshkwrkhptqvcmylyvvykwjhgknmsuolomginxdfwvqpfwlpwvommjjymsunxmbjxlcznmefzvuckeqfpighnxzxdpdlcifxbzldjctrswxmrxcjbbtivfnwqelhkmbunsroodysywhjsysajsrngtsvimguuwaicmuqzmafocvdzudgkmmvhydmafxqrrpkvvnnjyzohjwtjgqbrptggknxpuatfycatgimywhbafhjazjklgzxaiecmqbqgwgdepfspuxakrowawfolujdcyqsmakrkiqiduitooygdduztcquxqyraxhwjkvybbyiksqyqxqfmyzjyxxrxktmfklcjsjeijjflvtjayqlfuqtacxrfbrsdqtuwmflpdtxtjezsgeoeeyhcpncbknslbexvicfxslnqbelcfjonoakbitkizdlmusmydyajmiiouvqhhpmjspwoprvajocrloqydqbrgzxqafbfonuvecxjcrpoiorfqxofionzmomccxkhjqzkvpdevkwpsikonjxfthvtorexdyntvhttbtygzmtrrzprsgqnvbzhxuiruhugtaogfrjqdxnilxatjyltpbchjlkajaxefdjjwhqzjeejznbjkhdjqoltccfgosuuxodgyhvufwdrdxtpuvxlthxibekzkdoufkbstuxhwukrfaqsbratipaaxjawndpognykgltxofqbypomdpdsgncggpoddzbobloikifupdfgytydhxoxtcyerqpgezsddndikvcwufcefpdkdgvrlmvoiadawofsuyezliebpixyqboteavtvqeojxmemrdbptsxdckszxjgveaqngboxfdxqdgddczdzpyhlztthvbzgutaioqswwpzupddayzktwvqyvxcflmolxyewseqrrvpovpeftwgiywoyflwejpffxpubejlwmazjzfcldadgnkkjtmxktuzlocvqhjajqrfrfaloychnmokakwsfkrtacwjgsieptnujtgbbwzllvkpeuewegmkchhaaaptmbmoybtdotctkfyumafregkthibmufiudjrcohdhuhlpjeishhekicdfiiostjmofwhreoegrnbqgkhmiezgtasdaqdcixsrdfdsfcrgjaryeqtkussultserwmyealuvxckhcgojsxzsfxmrtcfhqpowalbbzvpcltiwdhexbvcjojdptxeplgestsnpmpibymzaolqaybmeezyagvvftcuqgqrpjauxjnmudeasbpeormqofrbmmgorysyztkbloyfjikxdrytsdfdrjagghbbjqkujemzvvtioluzitrmaxjphducstlearfirqknijfdurdztizvwoeqzamxkbbvmnbxomhsxfmwdhocdyabcygzojqebxferyieqfislcpwiaadbarnsgnuvhkaidexxcgxhmvsiwqhoxkjwvycbyaqiddlrgsvqvzkvqzeewbxnfqlhavmqyucnnlskzyhwlnpglakbstcsnmsipeekjbwvokjjasfcruinzkcmjtkuztnglqakavnjmvccjgquzfftcqzwnrvywoqxhzbkbjufjuyqqqtaoakzbykeraqalcqzuhjndgusnvdanqrwemqsmcwxelogrfxxsdyzlbfuvopxsyzuizshrtauculajiapoentvnkxpvyfxfecjolvlezsmfmibhptmgdkiucnsralqhtutgvnpzicjwcgrtcgyueuqsxnyspxmnzhupjwalphkutczrptfxsvgeikwqqhesezmkoliizhceciotrcrjhunyfnpeyrnmucyhkozbipsmuqfgujshzhzuxextaapmrbhvexaqyifwrodhftkwbpyndylvfukebddabmjperimjtzeeqwmjzjxjrqglwcsuxinztzxpzfdlirmyroecjkimmgnybedfhssjfzzdnqlzihfgobikowitiqdyzlhxbxifamfkeienxqvcmvhzixicqlylurlfnzbrfoztfjxswwlxkvrhueccohddaazuluirluhzliuqeqiajvmvtbpibfhiulyagqfowibqjkjewqminwsuupmxnijyrbiodfknndgpfiannwlkillxmirfqmmoktexmoqxqujogmxjmkenfphffmdfablsaqxufjwvmufogrzjarlopjhidbfbhoivkknzgqresjprfknjetohwtqurxyngxilywmbgpsctswswwkasyisochqeslbiunnbgxsgzwkopnhgdjyuherwtrkypbjrdesztgkxzueqrhhicwndmidmqahdwcycqpgtuildbowqhjaqnmblbnvvsxahycecvfnbvqzcjburykyjkgazgauobvieoerphnehdjxfianvcaasrctenrcwcgzcqbzufwsqllzbxnjzktgermrodlzuvkdblqcwbfjevjkygbgoalqyibexruhsxsowmchcogiffedbuddithpwocmovwbpvxzhwmyzpuwdhrorlqxxtqtwswmdcszbxwyirhpwjjulqoovmgqydxctjrnncsfevitouvdvsgdftpyjztxrxhuggdtyfandnuvufixthdxidrlzzkssngvrmtkwzifwjoqyawcohqxrucjixdcrhgybujxpbjfwxunbbotjlijfagrdsbeemkvgaebuagweegcgpoleicaakefhgvgjislsamatuqmmjisifffwmigqwxaywwmoyzarwtpiimekzofbycyoqznbnqwnncmzoiwpjgpymvynrgasxpekunmzksdrfxlyxewqmfoeufccrwevhhxxjqzkptkctaqerwotatqgkbnjqbpfyglucttnmxpxrrjhglbmzzjtyupaexfismwrvfgtunlriabhhyklpmevgmltnkdttjmemegytzzikcykidlasvugyzfaozknksednbsdcfnfwtozioavvipvsrkztslcxqgrccocxtwnxobbhidcublbnpwhohqjcxwfftmptlwtpjugbchgxahplumbjqjfvljhqzmbdsdeemxevugsthrveucyqxdktkdymznwdvkuoytvfrrfzrmlnedhckhngadcpugwzfupcudmukkpzrtdqvpcpzspuhdfoeojybisjmcjmcyhiiqjnfkcpepbflwfwmorpgwumlzynzpbbvvrgtxpsgzdelmlohavhyqhrfztmncnllnfdgdotoiojwtwilwwdszhcqbkdwtyrurxkzgcwrcvqlhynujihfdbwnnhkwdmfwciurvrqkmyghvhftbfhjogfrrslmuzussufwkkiewfevkvgalhyutnfxzgxbifjhbqolbsanvwkhyfxywfbvxvoiwcqhvdypwpgquutrugldizlvqaeeboriznjxovvmbwqyrxmxqilplplszubphmeszzrfjoliuskludoukazpiezpzucrsiiiichlxthowlcbmmfnyjyylgrcseraqtwodnxvugpysbosancqgzmxinonoeqmvyumsdwjncgztbepamqupqvxzudrniawehxilhybtdsupswxzjfhhchdeqoidvigjhkonfrdskxvoskgezzhhcpcfodahrlnkoldcdomllfcywrtqofedeychinhsvcssmgbadabdgyvmscucbckahgjawopdwlixbkmlxcpxtaqoempcldkefcerzeiowhgyhreveztowuigsgwcvdjahrfvrvvubliwretdwqslwgusqoqcczbzdalaocaarmtqhgjtzjjwnntuezwioelmwxnvnfeeggjljuybgshzeqsongxutyjovbklauknymkkkmnnwqxixaiwaxfbysglyvazrrcqcbgepgegwlmtycljiaqivlscezkquxkgzubqnbdsfxditryyagiihyoqdhtudnfmkwaohttygtwesumjjivazppjzkbdywdfudbjkubytrfasxkxqmdgnirqronvypulppeaqbjimtvffglxvihsvesvhbagtuikytbocsjnxfoxmtwpfwcdadliexyisjopbkqbjhlflqyxnjdkqndjpbdehwfsljapruwbslzchkyvsmcvocictzqxcktfmoathqnxmlqirfjezhqbboupnzlyqmiqiqkkbhwhpcyibipmizzxhlbjffxdzigymhjgyowmrjouvfjwgyzdovyslmfbplvjnqvfdbfeqvugoqdzvtggrpueutlljsfgudmgrzjqiaghatyzwjbkxxadrwjohhqmnwrswodapavdwyvwicbignxagbqodjeihgvwbdlexjcrltkidjdzjjteihgwedogtxafmajjgfgprbtbktqvirgxvvakqhbvgizxdgmabszclfbkrchaubgcobhpqrtfjbjzhpllxyvuqinnnkzdwqxzjjbniytymygnjzmklhpvazfqcdhafvoxlkxnvsmzfhjcqwdzqmlblhduduwbpbwonfmfwwbvhbgoyhwlmlxfnhlfpzwiybgeqghufeqilmdxzcdwrdwiculhnhzxybxvkwpjbwyprvtphhhqsnukanpnzoxtumxwlgostwbgqmtvdzsecquyrircmlckkzviczrvtkzyazlihddrlohyrovhprvcsmjrbxjaivvgolidxbyvxgkflallznsylhuzrkhrvfakpbhwhrgtwnlczewkyxhcturbfbfvlwvhaykumdftqbkmdxutbnphdsgplxxsdkcfouaprhecugnzdsjdyjkkuvtjtberlrwxhddmshcoyzlrgwugpnozubiglbcjwxjnvnmnbdtvlfbqqijwmdkrzslhsvnxnrsdbkbyxfkluvtofyesakxclxvodsuxwlyqkoyhynxfmpvmecqxxasvmsdrandljnyeepxaiwdvmmrzxstnzzfkxjsflkkrabqkicjutpyrbaewqzwfwdhzjqibmqhhzbnoaucsbpjtvvumkpaehnxxsjgkfpbfannzznhylowtsnilprqrbohrmcucboxzqwnbkbkgldydkqqqgjbtxavejjlxfqweybeaczszapiqiqoqwzhrvnjlmjmdmyyziqcusbpyxqwetclyrhfjrgzxbydajuqnbxhmjgenskqjikmgqlpbmsvuuxehfbydyqvgdfnkdqhlptgaollttiduybwqgaaatmcvdhagbusjrjigyhcphyhowixnezvioigsjdosikthzijrdvsfabprlcmjtjekculxcoyvypsozolqezlgunkhsftyjrffpfkuxbuoolragvarmtjozwqfiqdlaldxdauwzdrlhxlghtovdwesahmzklfoywukjufdiyiepnyjqzqbvomvefaahlnbgjhvumffksfvomrbnfstssvdgpubtmglxicclsijqumvibauoaxvgteljaajfcrqadkxbqrgbwaihxdsaisopmmwbzddapbczwnfnxspgtajjswcubnspwxglemattdgijkavsoanafyrkczcvmxzciuvtiwnraibtfrdqcntksioxjlzstxivizavgurmvwphdfxcvwqicctqicommgehtlunpbknkkklbzcjrxcxjchbszlqhtcdkzbdktkffbbwufcvscjsaraktaatyexzjxvxvoyyzivxpmwuxxkjdkrrmfegzkevmaeotwvpcrjtbfsblfdebacvomgtudrlcrjktvwdaerlafaqfcopbqxujngvxmjelcuesauyxuazrhiztlapgvsdenyqpafckjzohjjbdosjyvombptrppmanummqvahchtqkjdppwwskbygzaqpjlxkiposgfwltwlkvowynkcytprknckyppzvjjqaqibhakstpgkpbhviuqdrnsazdfptdmheqeusmkskdldaqnxthokukmhcpssjrtjnemyvlsaeryoeiclipnrjmbiyzpzfprjeyhphuqtdgqsgmicalezpyoakygeorrhzuyzhqqddhrygeybtoanobkvbfgpchrbtqbampimgefkyrkdfqgwyulvqbzljzbrisjugfjpruwilxneypgflzfldsbkpymcmxfpedmwogtxqrifposbwmohakknpkdbdycsgetahejtlqjaoumqyjbxywbmpbtcgquedhtfbbptomabbnahguvzsayqgvqxolvuflfjfhvmilqdzwqusvlcgemlaouwlgluuqtrqlhwooretsjjtnpnvrpnicakqcfuxotzmvqhsvoptvqiletevbhfbrolhijwidauovqlnqwmwvfoxljrbjtbwuazkhpnxntigrbdlhwbtwtzlnginyooppgpilsuzzjvfhanrggtxcjfxmvgbfsipktduomcoukthptkxahkkivmbnikapysfahapdembxvuakdniziuslabaotlifsolqboplhuasrlawpjsjaheapmubdtysalursciiukkgtrkzmqaltyksvdmomgydqqswpkqmewzzyxifqiivisommszulngjdsovkgsahicjhnlxqutcsyhfhxxyamenvwbruzzkywgmcmnqzvkindlsworliooqshsbxvoctrjionbzsihjhfitybhqyajludzdmitakuritzrgpdkvqptsmrqojcagmrhjppgsovqgrgjzdpzmjcrjbqprzbuufhwjlfgjwokimhvihgkgnkuajkpfsbiragdwbggbjesipyihpinhcrhpobdiaasfdivbsjpqeobgbzszqdkoixnhihncdutlggytzukcbtrdvxgbdllkswarjqehcdddgqdvwxgjtyymecyvqsutnpnwygxvlxxrpggidpmoygidulrdnixkuuiwmigcsntnlvomivajdmmopbyqljbmkqueawblhaicmshjhwnxieiftzjwwrwameuuzcoqiuibpcsaajzdciyxsqaeubgixinvwlecbkrctrwtoskgbdjbyjlgvmydlqrymdhyfdqawurvxprrnfnymfuvenrfdwpnxfqsbylqfokjnmpvnrtoqnhzpgzsebieouetuuruwenrjbuwondepkkuvxfzyswbnlykxglazitalhyhtksszzhglorprfobxkihnwxghhybaaspqmucv"
#d = "xuumbjffxuzovdwrnolopeingppzgorotzdqfprokkmucxwsub"
print s.checkInclusion('ab','eidbaooo')