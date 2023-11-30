#!/usr/bin/env python3

import argparse
from ctypes import sizeof
from math import sqrt
import sys
import numpy as np

sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv


def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite


    #Calculating Fitness using Ulysis
    #print(activity_mat)
    (rows, columns)=(activity_mat.shape[0],activity_mat.shape[1])
    transposed_mat=activity_mat.T               #transposing the matrix just to make column wise iteration easier
    W=[]                                        #to store Wi values of each component
    for i in range(columns):                    
        component=[]
        L_val=0
        component=transposed_mat[i].copy()             #copying the component 
        if(np.all(component == 0)):                    #if all entries are zero then Wi=1
            W.append(1)
            #print(1)
        else:
            for j in range(columns):                   #to check how many components are same as our component
                if(i!=j and np.array_equiv(transposed_mat[i],transposed_mat[j])):
                    L_val+=1
            W.append(L_val/(columns-1))                #Wi= number_of_Li/(number_of_components-1)
            #print(L_val/(columns-1))
    W_ulysis=sum(W)/len(W)
    #print("ulysis=",W_ulysis)
 
    return W_ulysis


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.
        #calculating suspeciousness using ochiai score
        activity_mat=self.activity_mat
        error_vector=self.errorVec
        comp=[]
        for i in range(len(activity_mat)):
            comp.append(activity_mat[i][comp_index])
        cf=0
        cp=0
        nf=0
        for i in range(len(error_vector)):
            if(error_vector[i]==1 and comp[i]==1):          #Number of failing tests that execute Component
                cf+=1
            elif(error_vector[i]==0 and comp[i]==1):        #Number of passing tests that execute Component
                cp+=1
            elif(error_vector[i]==0 and comp[i]==0):        #Number of failing tests that do not execute Component
                nf+=1
        denominator=sqrt((cf+nf)*(cf+cp))
        if(denominator):                                    #if denominator isn't zero then calculate ochiai otherwise 0
            ochiai=cf/denominator
            sus_score=ochiai
        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        rankList = []

        # ToDo : implement rankList
        component_scores = []
        activity_mat=self.activity_mat
        error_vector=self.errorVec
        (rows, columns)=(activity_mat.shape[0],activity_mat.shape[1])
        print("\n\n\n\n")
        print("Optimized Activity Matrix:\n",activity_mat,"\n")


        #to calculate the suspeciousness score of each component and sort the list in descending order of suspeciousness
        for i in range(columns):
            score = self.suspiciousness(i)
            component_scores.append([i, score])
            sorted_components = sorted(component_scores, key=lambda x: x[1], reverse=True)
        #now the sorted_component will be like [[0, 0.7071067811865475], [1, 0.7071067811865475], [2, 0.6666666666666666], [9, 0.6666666666666666], [4, 0.5773502691896258], [5, 0.5773502691896258], [8, 0.5773502691896258], [3, 0.5], [7, 0.5], [6, 0.0], [10, 0.0]]
        
        sorted_components = [['c' + str(i), number] for i, number in sorted_components]
        #Just made sorted_component as [['c1', 0.7071067811865475], ['c2', 0.7071067811865475], ['c3', 0.6666666666666666], ['c10', 0.6666666666666666], ['c5', 0.5773502691896258], ['c6', 0.5773502691896258], ['c9', 0.5773502691896258], ['c4', 0.5], ['c8', 0.5], ['c7', 0.0], ['c11', 0.0]]
        

        #Now i am counting the components with same score
        score_counts = {}
        for id, score in sorted_components:
            if score in score_counts:
                score_counts[score] += 1
            else:
                score_counts[score] = 1
        same_score_id_counts = [[id, score_counts[score]] for id, score in sorted_components] # Generating the list having each elemet as  [component, number_of_components_with_same_score].
        #Now same_score_id_counts will be like [['c1', 2], ['c2', 2], ['c3', 2], ['c10', 2], ['c5', 3], ['c6', 3], ['c9', 3], ['c4', 2], ['c8', 2], ['c7', 2], ['c11', 2]]


        #Now i have to make ranklist as [['c1', 2], ['c2', 2], ['c3', 4], ['c10', 4], ['c5', 7], ['c6', 7], ['c9', 7], ['c4', 9], ['c8', 9], ['c7', 11], ['c11', 11]]
        #i.e. just rank will be worst case rank 
        #explanation: here c1 and c2 have same score hence assign them rank 2
        #             c3 and c10 have same score hence assign them rank 2+2 i.e. 4
        #             why 4? answer-> 2 ranks already used now there are two components with same score hence assign them rank 4
        #             c5, c6, c9 will have rank=4+3=7 i.e. 4 ranks already used and there are three components with equal score hence4+3=7
        #             similarly ranks for other components are also calculated. 
        rankList.append(same_score_id_counts[0])
        for i in range(1,len(same_score_id_counts)):
            if(sorted_components[i][1]!=sorted_components[i-1][1]):
                rankList.append([same_score_id_counts[i][0],rankList[i-1][1]+same_score_id_counts[i][1]])
            else:
                rankList.append([same_score_id_counts[i][0],rankList[i-1][1]])


        print("error Vector:\n",error_vector,"\n")
        print("components with their Ochiai scores sorted in descending order:\n",sorted_components,"\n")
        #print("count of components with same score:\n",same_score_id_counts,"\n")
        print("final ranklist:\n",rankList,"\n")


        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
