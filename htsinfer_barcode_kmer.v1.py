"""Infer potential barcode k-mers from sample data"""

import pandas as pd
from enum import Enum
from typing import List, Tuble


class Outcomes(Enum):
    invalid_number_requested = "invalid_number_requested"

def group_kmers(input_kmers: List[str], kmer_base: str,
                position_dependent_frequency: float = 1.0) -> Tuple[str,float]:
    
    """Function that groups kmers by position-dependent frequency. 
    Quantile based discretisation method
    
        Args:
            input_kmers (List[str]) : list of kmers
            kmer_base (string) : Bases of kmers
            position_dependent_frequency (float) : Position dependent frequency in decimals,
                if not exceeding maximal value.
            
                
        Returns:
            sorted_dict (dict): paired motif frequency {motif: frequency}
            
    
        Raises:
            TypeError:  'input_kmers' is not a list
            TypeError:  'kmer_base' is not a string
            ValueError: 'kmer_base' is invalid (only A,C,T,G)
            ValueError: 'max_position_dependent_frequency' is 
    
    
    """
    
    # validate kmer character input parameters
    if kmer_base != ["A","C","T","G"]:
        return Outcomes.invalid_nuc_requested.value
    
    # validate numerical input parameters
    if position_dependent_frequency <= 0:
        return Outcomes.invalid_number_requested.value
    
    
    
    
    kmer_frequency: Tuble[str,float] = {} # Create empty dictionary (str -> float)
    
    for kmer_no in range(0,len(input_kmers)):
        kmer = input_kmers[kmer_no]
        
        # valid kmer bases
        valid_bases = 
        
        
def kmer_size(input_sequences: List[str],
              kmer_length: float) -> List[str]:
    
    sequence = input_sequences[]
                

def                 
                
                
                
                
def measure_similarity(input_kmers: int)
