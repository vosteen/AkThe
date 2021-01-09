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

* research gap
    * Spezielles Problem: $sign\big(\sum_i(sign{(x_i)})\big)$
    * Verbund von zwei Garantien (DP/SMC)
        * aus vorhandener Froschung zu Datenschutz in maschine learning motiviert (DP)
        * Anwendung auf SMC für verteiltes Lernen
    * macht Kooperation von mehreren Instituten mit geschützten Daten möglich
    * Schutz gegen
        * membership inference (und ähnliche) durch DP
        * neidische Institutionen (SMPC)
    * DP wird durch umgebendes Problem gewährleistet
    * in dieser Art ungelöst -- das harte ist, das Zwischenergebnis zu schützen
* neuer Ansatz mir logischen Verundungen
    * erfüllt die Anforderungen
* er läuft zuverlässig, ist jedoch sehr teuer


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

* SMPC
* Optimizer/maschine learning/...?
* MPyC




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

* wir lösen das Problem mit geschickter Umformulierung
    * Zusammenfassung von $sign(\sum(b_i)))$ zu $\binom{n}{\lfloor\frac{n}{2}\rfloor+1}$ einzeln überprüfbare logische Ausdrücken:
        * die Ausdrücke bestehen aus jeder Kombination von $\lfloor\frac{n}{2}\rfloor+1$ (etwas mehr als die Hälfte) der Elemente, die miteinander verundet sind.
        * Wenn der erste Ausdruck $1$ ergibt, wird __1__ als Ergebnis zurückgegeben und das Evaluieren sofort abgebrochen.
        * Bei negativem Ergebniss aller Läufe wird __-1__ zurückgegeben.
* Voraussetzungen sind $n$ Rechner/Prozesse, die in direkter Kommunikation zueinander stehen
* todo: Architektur kurz erläutern
* Performanceanalyse mit Kommandizeilenprogramm _multitime_
* Evaluation durch Test und Gedanken



## Results :penguin: 
:::info
Here you will present and discuss your outcomes: implementation results or measurements or other project outcomes 

    Evaluation / Results:
    ○ Data analysis
    ○ Experimental results (objectively describe the results)
    Interpretations:
    ○ Interpretation w.r.t. the hypothesis

:::

* Ergebnisse (Rohdatenbezug -- geht nur mit bis zu 11 Teilnehmern realistisch, Laufzeit exponentiell,...)
* Interpretation:
    * geht nur effizient für sehr kleine Personenkreise ($\le 5$) -- dann aber gut



## Conclusion
:::info
    Conclusion:
    ○ Summarize your thesis again as in the introduction. Describe how your
    evaluation revealed that your system is successful. Describe future work in 
    this area.
    Future work:
    ○ Open problems that should be worked on
:::

todo

## Referenzen






