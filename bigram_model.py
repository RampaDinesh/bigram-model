import torch 
from torch.optim import Adam
import torch.nn as nn
from torch.nn import CrossEntropyLoss
from collections import defaultdict
import numpy as np

database=[["dinesh is the gratest man in the world"],
          ["he is the biggest fan of elon musk"],
          ["he is genius in programming"]]
new_db=""
for i in database:
  for j in i:
    #print(j)
    new_db+=str(j)
  new_db+=" "
#print(new_db)
new_db=new_db.replace(' ','.')
new_db=new_db.split('.')
word_index=defaultdict(int)
index_word=defaultdict(str)



'''for i in range(len(new_db)-1):
  print(new_db[i],new_db[i+1])'''

unique=[]
for i in new_db:
  if i not in unique:
    unique.append(i)

#print(unique)

for index,value in enumerate(unique):
  word_index[value]=index
  index_word[index]=value

#print(word_index)
#print(index_word)
training_data=[]

for i in range(len(new_db)-1):
  data=new_db[i]
  target=new_db[i+1]
  data_index=word_index.get(data)
  target_index=word_index.get(target)
  training_data.append((data_index,target_index))
#print(training_data)
training_data=torch.tensor(training_data)
input_tensor=training_data[:,0]
target=training_data[:,1]




class word_predictor(nn.Module):
  def __init__(self,vocbal_size,embedding_size):
    super().__init__()
    self.embedding=nn.Embedding(vocbal_size,embedding_size)
    self.linear=nn.Linear(embedding_size,vocbal_size)
  def forward(self,input):
    embedding_vectors=self.embedding(input)
    lin_vector=self.linear(embedding_vectors)
    return lin_vector

model = word_predictor(vocbal_size=len(unique),embedding_size=10)
ln_loss = CrossEntropyLoss()

optim = Adam(model.parameters())
for i in range(1000):
  optim.zero_grad()
  output=model.forward(input=input_tensor)
  loss=ln_loss(output,target)
  loss.backward()
  optim.step()
  #if(i%100==0):

    #print(f'i:{i},loss:{loss}')


generated_text=[]
generate_len=int(input('enter the length '))
input_=input("enter your start word ")
generated_text.append(input_)
while len(generated_text)!=generate_len:


  user_output=model.forward(torch.tensor([word_index.get(generated_text[-1])]))
  max_value=torch.argmax(user_output).item()
  generated_text.append(index_word.get(max_value))
generated_text_data=" "
for i in generated_text:
  generated_text_data+=i+' '
print(generated_text_data)

  
  

