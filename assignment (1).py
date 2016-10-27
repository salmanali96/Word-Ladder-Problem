import sys
from collections import defaultdict
import json

class Words:

    def __init__(self,name):
        self.name = name
        self.adjacents =[]


class Queue():
    def __init__(self):
        self.queue = []

    def Enqueue(self,item):
        self.queue.append(item)

    def Dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue == []

def checkinlist(list,start,finish):

    if list:
        numrows = len(list)    # 3 rows in your example
        numcols = len(list[0])

        #for j in range(numcols):
        for i in range(numrows):
        
            if  start in list[i] and finish in list[i]:
                str = 'Path Already Known in list'
                
                return str

    return ' '
def breadthfirst(start,finish,Graph,dict,list):

    list1 = []
    
    check = checkinlist(list,start.name,finish.name)
    str = 'Path Already Known in list'

    if str == check:
        #str = 'Path Already Known in list'
        #print(str)
        return str
    

    if start.name in dict: #or finish.name in dict:
        if dict[start.name] == finish.name:
                print ('Path Already Known')
                str = 'Path Already Known'
                return str
    
    if finish.name in dict:    
        if dict[finish.name] == start.name:
            print ('Path Already Known')
            str = 'Path Already Known'
            return str

    parents = {}
    q = Queue();
    q.Enqueue(start);
    parents[start.name] = None

    while (not q.empty()):
        node = q.Dequeue()

        for neighbours in node.adjacents:
            n = neighbours.name

            if n not in parents:
                parents[n] = node.name
                list1.append(n)
                if n == finish.name:

                    list1.append(finish.name)
                    dict[start.name] = finish.name
                    list.append(list1)
                    return parents

                q.Enqueue(Graph[n])  #change
    
    str = 'There is no Path'
    return str
    #print (parents);

def getPath(start,finish,parents):

    finishnode = finish.name

    path = [finishnode]

    if finishnode in parents:
        node = parents[finishnode]

        while (node != start.name):
            path.append(node)
            node = parents[node]

    else:
        "There is no Path"

    path.append(start.name)

    return path[::-1]


def BuildGraph(file):
    w = {}
    wordfile = open(file);
    words = wordfile.read().split('\n')
    max = 0;
    for word in words:

        for i in range(len(word)):
            if max < len(word):
                max = len(word)
            wcard = word[:i] + '*' + word[i + 1:]

            if wcard in w:
                w[wcard].append(word)
            else:
                w[wcard] = [word]
    
    for key in w:
        wordlist = w[key]

        for word1 in wordlist:
            for word2 in wordlist:
                if word1 != word2:
                    DrawGraph(word1,word2)

def DrawGraph(word1,word2):

    if word1 not in  Graph:

        word = Words(word1)
        word.adjacents.append(Words(word2))
        Graph[word1] = word
    else:
        neighbours = Graph[word1].adjacents

        if word2 not in [x.name for x in neighbours]:
            neighbours.append(Words(word2))

    if word2 not in Graph:
        word = Words(word2)
        word.adjacents.append(Words(word1))
        Graph[word2] = word

    else:

        adjacents = Graph[word2].adjacents
        if word1 not in [x.name for x in adjacents]:
            adjacents.append(Words(word1))



def createwordfile():
    fileObj = open('words.txt','w');

    with open('dictionary.json') as dictionary:  # Loading dictionary file.
        print ("loading...");
        myDictionary = json.load(dictionary);
        print ("loading...");
   # print (myDictionary['MACROCHIRES']);
        for W in myDictionary:
            fileObj.write(W);
            fileObj.write('\n');

 
def createfiles(file):

    w = {}
    wordfile = open(file);
    words = wordfile.read().split('\n')

    for word in words:
            length = len(word)
            filename = str(length) + ".txt"
            file1 = open(filename, "a")
            file1.write(word);
            file1.write('\n');

        






if __name__ == '__main__':

    createwordfile()
    list = [ [] ]
    freq = {}
    freq = defaultdict(lambda: 0, freq)
    min  = 100
    max  = 0
    Graph = {}
    dict = {}
    file = "words.txt"
  # createfiles(file)
  # print('OK hogaya')
    list = []
    BuildGraph(file)

    choice = input("1)Traverse all the Words in Dictionary      2)Hard Coded word:  ")

    if int(choice) == 2:        

             word1 = 'COLD'
             word2 = 'WARM'
             if word1 in Graph:

                start = Graph[word1]
        
                if word2 in Graph:
                    finish=Graph[word2]
                    dict23 ={}
                    list23 = []
                    predecessors = breadthfirst(start, finish, Graph,dict23,list23)
                    str = 'There is no Path'
                    if str != predecessors:
                        

                        path = getPath(start, finish, predecessors) 
                        str = ''

                        for p in path:

                            str += p + ' -> '

                        print (str[:-3])
                        sys.exit()
                else:
                     print("Word2 not in Graph") 
                     sys.exit()

             else:
                print("Word1 not in Graph")
                sys.exit()
           
    elif int(choice) == 1:
        found = 0;
       # word1 = 'HYPSTASIZE'
       # word2 = 'SHYPERISMS'
        notfound = 0;
        #start = Graph[word1]
        wordfile = open(file);
        words = wordfile.read().split('\n')
        words2 = wordfile.read().split('\n')

        for word1 in words:
            if word1 not in Graph:
                notfound = notfound + 1
                continue

            for word2 in words:

                if word2 not in Graph:
                    notfound = notfound + 1
                    continue;
                if len(word1) != len(word2):
                    continue;

                if word1 == word2:
                    continue


            
                if word1 in Graph:

                    start = Graph[word1]
                    if word2 in Graph:
                                            
                            end = Graph[word2]
                            parents = breadthfirst(start,end,Graph,dict,list)
                            str = 'There is no Path'
                            str1='Path Already Known'
                            if str  == parents:
                                notfound = notfound +1

                            elif str1 == parents:
                                found = found + 1

                            else:
                                found = found + 1
                                path = getPath(start,end,parents)
                                str = ' '

                                for P in path:

                                  str = str + P + ' -> '
                            
                                length = len(path)
                                freq[length] = freq[length] + 1
                                if length > max:
                                    max = length
                            
                                if length < min:
                                    min = length 
                                #print (str)
                        
                    else:
                        print("Word 2 not in Graph")

                else:
                    print("Word 1 not in Graph")
         
    else:
        sys.exit()

    print('The min chain is: %d' %min)
    print('The max chain is: %d' %max)

    print('The number of words found is: %d' %found)
    print('The number of words not found is: %d' %notfound)
    print (freq)

         