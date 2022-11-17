#This question includes the topics that hash table, string, dynamic programming, trie and memoization.

#Memoziation :

#Hesaplamada, notlama veya notlama, pahalı işlev çağrılarının sonuçlarını depolayarak 
# ve aynı girdiler tekrar oluştuğunda önbelleğe
#  alınan sonucu döndürerek öncelikle bilgisayar programlarını hızlandırmak için kullanılan bir optimizasyon tekniğidir. 

#Memoization effectively refers to remembering ("memoization" → "memorandum" → to be remembered) 
# results of method calls based on the method inputs and then returning the remembered 
# result rather than computing the result again. You can think of it as a cache for method results. 
# For further details, see page 387 for the definition in Introduction To Algorithms (3e), Cormen et al.

#Trie : 

#Bilgisayar biliminde, dijital ağaç veya önek ağacı olarak da adlandırılan bir trie, 
# bir küme içinden belirli anahtarları bulmak için kullanılan 
# bir ağaç veri yapısı olan bir tür k-ary arama ağacıdır.

#trie ile search algoyu yazıp ,memoization ile de bulmak lazım 

class Solution:
    def wordBreak(self, s, wordDict) :

        temp=None 
