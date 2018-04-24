import os,shutil,argparse

parser=argparse.ArgumentParser()
parser.add_argument('--user-name','-u',default='AlphaGoMK',type=str,metavar='N',
					help='windows user name')
parser.add_argument('--threshold','-t',default=0.1,type=float,metavar='W',
					help='File size threshold, greater than x MB')

args=parser.parse_args()
path="C:\\Users\\"+args.user_name+
     "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
respath="C:\\Users\\"+args.user_name+
        "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\Images"
threshold=args.threshold # 0.1MB

if os.path.exists(respath):
	shutil.rmtree(respath)
os.makedirs(respath)

count=0
for file in os.listdir(path):
	if(threshold<(os.path.getsize(os.path.join(path,file))/float(1024*1024))):
		count+=1
		shutil.copyfile(os.path.join(path,file),os.path.join(respath,file))
		os.rename(os.path.join(respath,file),os.path.join(respath,str(count)+".jpg"))

os.system("explorer.exe %s" % respath)
print("Saved %d files"%count)
