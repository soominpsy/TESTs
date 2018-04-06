#Author : JUNHO LEE
from matplotlib import pyplot as plt
import numpy
import sys,os
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *


def Basic_histo(filename, Xaxis_Name=''):

    if(filename[0]=="/"):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt","")

    infile = filename
    Mode = most_frequent_bin(infile); #print(type(Mode)); print(Mode)
    Median = c1_median(infile)
    Range = c1_data_range(infile);   # print(Range)
    Total_Entry = c1_total_ENTRY(infile); Total_Entry = int(Total_Entry); str_TE = str(Total_Entry)
    Mean = c1_mean(infile);  str_Mean = str(Mean)
    Var = c1_variance(infile);
    Std = c1_standard_deviation(infile); str_Std = str(Std)

    str_Mean = str_Mean[:len(str_TE)+2]; #print(str_Mean)    
    str_Std = str_Std[:len(str_TE)+2]; #print(str_Std)

    X_AXIS = []
    X_WIDTH = []
    Y_VALUE = []

    f = open(infile,'r')
    BinN = 0
    for line in f:
        _,xaxis0,xaxis1, yaxis = line.split()
        X_AXIS.append(float(xaxis0) + (float(xaxis1)-float(xaxis0))/2)
        X_WIDTH.append((float(xaxis1)-float(xaxis0)))
        Y_VALUE.append(float(yaxis))
        BinN = BinN + 1
#    print(X_AXIS[0]); print(X_AXIS[BinN-1])
    

    fig = plt.figure()
#    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0])
    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
#    print(len(barlist))
    for i in range(len(barlist)):
        barlist[i].set_color('b')
    plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9])
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
    plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
#    print(plt.ylim()); print(type(plt.ylim()))
    plt.ylabel("Entry Number")
    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)
    plt.title(filename_No_Txt)
    SaveName = filename_No_Txt + ".pdf"
    plt.grid(True)
    plt.savefig(SaveName)
#    plt.show()
    f.close()


def looping_Basic_histo(filenameList, Xaxis_Name=''):
    for filename in filenameList:
        Basic_histo(filename, Xaxis_Name='')


def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/concrete_tree_cut_concrete_f_fineagg_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"

#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree1_f_py_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree1_f_px_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree2_f_pz_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/concrete_tree_cut_concrete_f_strength_hist.txt" 
#    inputfile = "../root1_project.txt" 
    Basic_histo(inputfile, ".X-axis.")


if __name__ == "__main__":
    main()

