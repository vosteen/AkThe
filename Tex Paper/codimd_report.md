Das Projekt wurde von Lars Vosteen hierherverlegt, da der eigene Server gewartet werden muss.

# $\Sigma$ignum

## Abstract
todo

## Motivation
:::info
Know what you want to do and why that is interesting (maybe with bullet points). But do not write this section until you know what you actually have done so that the motivation fits your work.

    ○ Establish a research gap:
        ■ What is the problem, the problem space (PD)?
        ■ Why is the problem important that is covered in the thesis? What is the
            problem?
        ■ Why is it hard? What have others done?
    ○ How do we tackle the problem?
    ○ What are our hypothesis?
    ○ What are our techniques? How do you prove that the solution we came up with 
    is a GOOD solution? How can you demonstrate that your solution works?
    ○ What are our findings?
    ○ (Definition of terms)
    ○ (Description of remaining chapters)
:::

This research contributes to enabling multiple parties to collaborate with private data. To protect these against disclosure to each other or outsiders, the strong guarantees of _Differential Privacy_ and _Secure Multiparty Computation_ shall be adhered to.

The surrounding project by _Kummerfeld et al._ works on achieving _Differential Privacy_ while we will tend to _Secure Multiparty Computation_.

The step in the method of Kummerfeld et al. for retrieving and aggregating the private data is to be adapted such that each party participating in the calculation can only know their own data and the result (1 or 0) and thus comlies with the guarantee of _Secure Multiparty Computation_.

The model of a semi-honest attacker is assumed.


## Background
:::info
You should find and describe related work early on. Know what other people have done.

    Problem Statement (ca. 1 - 4 pages):
    ○ Related work (either here or before conclusion):
    ■ Describe the field in general and how others have tried to solve this
    problem
    ■ In which way is your way better for your hypothesis?
    ○ Describe in detail the problem you are trying to solve
    ○ (Hypothesis presentation?)
    Optional: Preliminaries
    ○ Introduce concepts / frameworks that you in your thesis
:::

### surrounding
The surrounding project by Kummerfeld et al. researches new ways to make machine learning differentially private.
Out of this research came an approach to let the training data decide for each dimension which half-space would best suit them by computing $\text{sign}(\sum_i\text{sign}(x_i))$ where $x_i$ represents the private data, which are arbitrary numbers.

### attacker model
:::danger
semi honest
:::

### MPC
:::danger
garbled + artithmetic circuits 
:::

### MPyC (todo: cite)
:::danger
ToDo inkl. Kommunikationsart
:::

### MPyC -- sign()-Funktion (todo:cite)
The sign() function in _MPyC_ uses an arithmetic circuit (todo: check) to compute the sign-function of a number (that can be an unpublished (intermediary) result of an other calculation).

The sign function is defined as: 
$\begin{equation}
\text{sign(x)}= \begin{cases} 1&\mbox{if }x>0\\0&\mbox{if }n=0\\-1&\mbox{if }n<0\end{cases}
\end{equation}$


First it uses the internal function _is\_zero\_public()_ (todo: footnote: This function itself uses an atirhmitic circuit.) to check if the value is zero.

If it is zero, it stops as it has its result.

If not, it obscures the value in signed binary representation with random data by using xor with random bits, leaving only the first bit untouched -- this can be either one or zero indicating a positiv ot negative number.


### related work
:::danger
* MPyC
* MP-SPDZ: A Versatile Framework for Multi-Party Computation – Marcel Keller
:::




## Work Description
:::info
Here you describe the work you have performed, problems you have solved and methods you have used. There is a fine balance between brevity and conciseness and ensuring that other people, if investing the time, would be able to reproduce your results given this description.

    Approach / Methodology:
    ○ Methodology:
    ■ How do you solve the problem (described in the problem statement)?
    ○ System design:
    ■ Requirements and specifications?
    ■ Describe how you implemented your approach. If it is a software system
    give diagrams, relevant algorithms etc.
    ○ System implementation
    ■ Describe the methods that we use, in particular the external methods and
    tools (background)■
    Describe your approach to solving the problem. Describe any potential
    weaknesses of your approach
    Experiments:
    ○ Experimental setup and design choices?:
    ■ Describe how you implemented the experiments.
    ■ Talk about the performance of the Azure instance during experiments
    ○ Experimental implementation:
    ■ Goal: try to make as concisely clear how you do you what you do
    ■ Motivate your design choices
    ■ Describe how you evaluated to show that your approach was successful.
:::

We use the python library _MPyC_ (todo cite) to calculate the results of function $\text{sign}(\sum_i\text{sign}(x_i))$.
This library allows two types of multiparty systems.
It can connect several processes on different computers or execute different processes locally on one computer in parallel.
In both cases, the data is protected from each other and bilateral connections use TCP.
For the evaluation of this project, the local variant is used.



The performance is measured with the python library _time_.
:::danger
performance analysis: explain what you did
:::


* wir lösen das Problem mit mächtiger Pythonbibliothek
* Voraussetzungen sind $n$ Rechner/Prozesse, die in direkter Kommunikation zueinander stehen
* todo: Architektur kurz erläutern
* Performanceanalyse mit Pythonbibliothek _time_



## Results 
:::info
Here you will present and discuss your outcomes: implementation results or measurements or other project outcomes 

    Evaluation / Results:
    ○ Data analysis
    ○ Experimental results (objectively describe the results)
    Interpretations:
    ○ Interpretation w.r.t. the hypothesis
:::

Our program (todo reference to appendix) solves the initial problem.
It uses an library for SMPC (todo: ref: glossary for this word and other abbreviations?) and scaleablebility was attained to allow it to be used in the intended usage scenario.

:::danger
computational complexity with figures
:::

It is therefore usable for machine learning and can be integrated into the intended scenario.


* Ergebnisse 
    * Anforderungen erfüllt
    * Laufzeit: (Rohdatenbezug -- ToDo)
* Interpretation:
    * ist für machine learning angemessen, da die teueren Operation (Verbindungsaufbau) nur selten genutzt werden muss


## Conclusion (do we need this section? - As it was not included in the original template -- I think not $\rightarrow$ delete if you concur) 
:::info
    Conclusion:
    ○ Summarize your thesis again as in the introduction. Describe how your
    evaluation revealed that your system is successful. Describe future work in 
    this area.
    Future work:
    ○ Open problems that should be worked on
:::


## References (bibtex kann ich gut erzeugen -> kann ersteinmal so bleiben)
* MPyC
* MP-SPDZ: A Versatile Framework for Multi-Party Computation – Marcel Keller


## Appendix
Code:
```python
from mpyc.runtime import mpc
import math


@mpc.coroutine
async def mpc_signumsum(input_bits):
    # compute sum and specify placeholder for result
    sec_sum = mpc.sum(input_bits)
    # compute maximum length of binary representation of sum (+1 as int() rounds down)
    bit_len = int(1 + math.log(len(input_bits), 2.0))
    # compute signum -- maximum length of binary representation is provided for better efficiency
    result = mpc.sgn(sec_sum, l=bit_len)
    return result


def prepare_list(input_bits):
    # define placeholder type as int
    sec_int = mpc.SecInt()
    # distribute secret data
    input_list = [None] * len(input_bits)
    for i in range(len(input_bits)):
        # each process finds its own data at the position of its id and writes it in its own secret version of the list
        if mpc.pid == i:
            input_list[i] = input_bits[i]
    # prepare special internal list with placeholders and secret data
    sec_vec_l = [None] * len(input_bits)
    for i in range(len(input_bits)):
        sec_vec_l[i] = mpc.input(sec_int(input_list[i]) if mpc.pid == i else sec_int(), senders=i)
    return sec_vec_l


async def main():
    # specify the secret data
    input_bits = [1, 1, 1, -1, -1]
    # start mpc and connect parties
    await mpc.start()
    # distribute data to parties and prepare list of placeholders for it
    placeholder_list = prepare_list(input_bits)
    # compute the sign of the sum of the secret data
    erg = mpc_signumsum(placeholder_list)
    # fetch the result
    result = await mpc.output(erg)
    # close the mpc connections
    await mpc.shutdown()
    # print result
    print("result of Sign(Sum(", input_bits, ")): ", result)


if __name__ == '__main__':
    mpc.run(main())

```





