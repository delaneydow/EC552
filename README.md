# EC552

## Authors 
Delaney M. Dow (programming contributer)
Hannah Collins (programming contributer) 

Emily Hill (team member)
Blaire Smith (team member) 

## Project Abstract 
Synthetic biology is an emerging multidisciplinary field that involves the synthesis of de novo cellular components. We designed a genetic circuit in Saccharomyces cerevisiae that utilizes molecular assembly kinetics to perform “input coherence detection”. These circuits can differentiate between two distinct input signals and detect when both are present, allowing for greater specificity and fine-tuned output control to make a synthetic circuit more akin to natural biological circuits. Our system leverages oligomerizing protein-protein pairs that can form both homodimers and heterodimers. Each oligomerizing domain is fused to half a synthetic transcription factor and controlled by distinct chemical inputs. In the presence of both input signals (i.e. hormones), co-expression of both protein domains drives formation of heterodimers to activate circuit output. Staggered induction will drive production of homodimeric complexes that delay circuit activation. Through a series of experiments, we measured fluorescent output in response to varied temporal input sequences. Our results indicate that allowing the first inducer to saturate decreased the time needed for heterodimers to form after addition of the second inducer. We also found that introducing both inducers simultaneously drove the fastest reporter response, while staggering inductions delayed heterodimer formation. We developed a computational model of our circuit based on protein-protein assembly kinetics and our experimental data to predict temporally-dependent responses of the system to varied inputs. By modeling our synthetic circuit under physiologically relevant conditions, we have contributed to the toolbox of synthetic parts available for future applications in vivo.

## Description
The following repository stores the code for the modeling component of our senior design project at Boston University, titled Designing, Modeling, and Constructing Coherence Detection Synthetic Gene Circuits Based on Protein Oligimerization. 
The modeling component was based on a series of three experiments conducted to be used as training data on our model of a series of ordinary differential equations. The training data optimized specific parameters in our equations, and the outputs of the system were predicted on a different set of experiments to test the model's accuracy. 

