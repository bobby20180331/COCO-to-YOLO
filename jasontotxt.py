import json
import os

def convert(data,name,json_path):
    for m in range(len(data['marks'])):
        # Get required data
        ct=data['marks']
        print(len(ct))
        for j in range(len(ct)):
            type=ct[j]['type']
            bbox=ct[j]['bandbox']
            print(bbox)
            print(type)
            if type=="猫":
                cls=int(0)
            elif type=="猫":
                cls=int(1)
            else:
                cls=int(9)
            print("cls:",cls)

                
            # Prepare for export
            txtfilename = f'{name}.txt'
            txtfilename=json_path+txtfilename
            content =f"{cls} {bbox[0]} {bbox[1]}{bbox[2]}{bbox[3]}\n"
            with open(txtfilename, 'w') as file_object:
                file_object.write(content)
# To run in as a class
if __name__ == "__main__":
    json_path='/data/ai/datasets/pet2k/devtest/'
    datanames = os.listdir(json_path)
    for i in datanames:
        filename=os.path.splitext(i)
        if filename[1]=='.json' :
            # print(i)
            filepath=json_path+i
            # print(filename)
            with open(filepath) as f_obj:
                data = json.load(f_obj)
            convert(data,filename[0],json_path)
