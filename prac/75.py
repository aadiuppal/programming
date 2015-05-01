class Solution:
    # @param {string} s
    # @return {string}
    def __init__(self):
        self.table={}
        self.max_v=0
        self.max_table={}
    def longestPalindrome(self, s):
        if len(s)<=2:
            return s
        l=len(s)
        for i in range(0,l):
            for j in range(i+1,l+1):
		if self.max_table:
			self.max_v=max(self.max_table.keys())
		if len(s[i:j])>self.max_v:
			if not self.table.get(s[i:j]):
		                self.check(s[i:j])
				print s[i:j]#,self.table.get(s[i:j])
        print self.max_table
        if self.max_table:
            self.max_v=max(self.max_table.keys())
            return self.max_table[self.max_v]
        return s[0]

    def check(self,s):
        if len(s)<1:
            return
        i=0
        j=len(s)-1
        if i==j:
            return True
        if j-i==2:
            if s[i]==s[j]:
                self.table[s[i:j+1]]=True
                self.max_table[len(s[i:j+1])]=s[i:j+1]
                return True
            self.table[s[i:j+1]]= False
            return False
        if j-i==1:
            return False
        if i<j:
            if s[i]==s[j]:
                if not self.table.get(s[i:j+1]):
                        self.table[s[i:j+1]]=self.check(s[i+1:j])
                        if self.table[s[i:j+1]]==True:
                                self.max_table[len(s[i:j+1])]=s[i:j+1]
                return self.table[s[i:j+1]]
            #else:
            #    if not self.table.get(s[i+1:j+1]):
            #            self.table[s[i+1:j+1]]=self.check(s[i+1:j+1])
            #    if not self.table.get(s[i:j]):
            #            self.table[s[i:j]]=self.check(s[i:j])
        return False

s=Solution()
a="rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"
a1="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print s.longestPalindrome(a1)
