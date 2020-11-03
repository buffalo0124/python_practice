"""Infer potential barcode k-mers from sample data"""

import pandas as pd
from enum import Enum
from typing import List, Tuble


class Outcomes(Enum):
    invalid_number_requested = "invalid_number_requested"
    invalid_nuc_requested = "invalid_nucleotide_requested"

def group_kmer(input_kmer: List[str], kmer_base: str,
                position_dependent_frequency: float = 1.0) -> Tuple[str,float]:
    
    """Function that groups kmers by position-dependent frequency. 
    Quantile based discretisation method
    
        Args:
            input_kmers (List[string]) : list of kmers
            kmer_base (string) : Bases of kmers
            position_dependent_frequency (float) : Position dependent frequency in decimals,
                if not exceeding maximal value.
                    
        Returns:
            Highly_abundant (Tuple[string,float]): Top 25 quantile frequency of kmers {kmers: frequency}
            Lowly_abundant  (Tuple[string,float]): Bottom 25 quantile frequency of kmers {kmers: frequency}
    
        Raises:
            TypeError:  'input_kmers' is not a list
            TypeError:  'kmer_base' is not a string
            ValueError: 'kmer_base' is invalid (only A,C,T,G)
            ValueError: 'max_position_dependent_frequency' is invalid
    
    
    """
    
    # validate kmer character input parameters
    if kmer_base != ["A","C","T","G"]:
        return Outcomes.invalid_nuc_requested.value
    
    # validate numerical input parameters
    if position_dependent_frequency <= 0 or 1>:
        return Outcomes.invalid_number_requested.value
    
    
    
    
    kmer_frequency: Tuble[str,float] = {} # Create empty dictionary (str -> float)
    
    for kmer_no in range(0,len(input_kmers)):
        kmer = input_kmers[kmer_no]
        
        # valid kmer bases
        valid_bases = 
        
        
def kmer_length(grouped_kmers: List[str], kmer_size: int, kmer_base: str
               minimal_kmer_size: int = 3, maximal_kmer_size: int = 20) -> List[str]:
    
    """Function that groups kmers by the length. 
    
    
    
        Args:
            grouped_kmers (List[string]) : list of kmer grouped by position dependent frequency
            kmer_size (integer) : Length of kmers
            kmer_base (string) : Bases of kmers
            minimal_kmer_size (integer) : Minimal kmer length, default 3
            maximal_kmer_size (integer) : Maximal kmer length, default 20
               
        Returns:
            List of sorted Kmer by the length
            
    
        Raises:
            TypeError:  'grouped_kmer' is not a list
            TypeError:  'kmer_base' is not a string
            ValueError: 'kmer_base' is invalid (only A,C,T,G)
            ValueError: 'max_position_dependent_frequency' is invalid
    
    
    """
                

def kmer_similarity()                
                
                
                
                
