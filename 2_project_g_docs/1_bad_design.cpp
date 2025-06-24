#include <bits/stdc++.h>
using namespace std;

class Document_Editor{

    public:
        vector<string> doc_element;
        string rendered_doc;

        void add_text(string text){
            doc_element.push_back(text);
        }

        void add_img(string img_path){
            doc_element.push_back(img_path);
        }

        string render_document(){
            if(rendered_doc.empty()){
                string result;
                for(auto ele:doc_element){
                    if(ele.size()>4 && (ele.substr(ele.size()-4)==".jpg")|| (ele.substr(ele.size()-4)==".png")){
                        result+="[Image: "+ele+" ]"+"\n";
                    }else{
                        result+=ele+"\n";
                    }
                }
                rendered_doc=result;
            }
            return rendered_doc;
        }

        void save2file(){
            ofstream file("document.txt");
            if(file.is_open()){
                file<<render_document();
                file.close();
                cout<<"document saved in 'document.txt' file"<<endl;
            }else{
                cout<<"Error :Unable to open and write in it.."<<endl;
            }
        }
};


int main(){
    Document_Editor editor;
    editor.add_text("hello world!");
    editor.add_img("pic.jpg");
    editor.add_text("this is an document editor");

    cout<<editor.render_document()<<endl;
    editor.save2file();
    return 0;
}