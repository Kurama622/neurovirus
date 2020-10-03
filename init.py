#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
###############################################################
# File Name: init.py
# Author: stubborn vegeta
# Created Time: Tue 15 Sep 2020 12:26:49 AM CST
###############################################################
import os
import numpy as np
import sys
import yaml

def conf(file):
    with open(file, 'r') as f:
        config = yaml.safe_load(f.read())
    return config

def to_head(layerSpace):
    return r"""
\documentclass[border=5pt]{standalone}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{mathptmx}
\usetikzlibrary{
    positioning,
    calc
}
\tikzset{
    subfig/.style={
        line width = 2.5pt,
        align=center,
        % font=\LARGE
        font=\Huge
    },
}
\def\layerSpace{"""+str(layerSpace)+"""mm}
"""

def to_colors():
    return r"""
\definecolor{VegetaRed}{HTML}{FFB6C1}
\definecolor{VegetaGreen}{HTML}{7FFFAA}
"""

def to_document():
    return r"""
\begin{document}
    \begin{tikzpicture}
      % \newlength{\mytextlength}
"""
def to_draw(i, maps, width, height, kernel, kernel_pre, height_pre, map_info, layer_info):
    if maps != 1:
        if i == 0:
            # 是否画巻积核
            if kernel:
                return r"""
                   \begin{scope}[xshift="""+str(i)+"""*\layerSpace]
                      % \settowidth{\mytextlength}{$"""+map_info+"""$}
                       \coordinate (start) at (0,0);
                       \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                       \\foreach \i in {1,2,...,"""+str(maps)+"""}
                      {
                          \ifodd\i
                              \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                          \else
                              \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                          \\fi
                      }
                      % \\node (outmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.25, minimum height="""+str(height)+"""mm*0.25] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / 8 * 7},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / 13 * 14})+(start)$) {};
                      \\node (outmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.25, minimum height="""+str(height)+"""mm*0.25] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1-""" + str(0.9/maps)+""")})+(start)$) {};
                    \end{scope}
            """
            else:
                return r"""
                   \begin{scope}[xshift="""+str(i)+"""*\layerSpace]
                      % \settowidth{\mytextlength}{$"""+map_info+"""$}
                       \coordinate (start) at (0,0);
                       \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                       \\foreach \i in {1,2,...,"""+str(maps)+"""}
                      {
                          \ifodd\i
                              \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                          \else
                              \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                          \\fi
                      }
                    \end{scope}
            """
        else:
            pos = (height_pre-height)/2.
            if kernel:
                if kernel_pre:
                    return r"""
                       \begin{scope}[xshift="""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)]
                          % \settowidth{\mytextlength}{$"""+map_info+"""$}
                           \coordinate (start) at (0,"""+str(pos)+"""mm);
                           \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                           \\foreach \i in {1,2,...,"""+str(maps)+"""}
                          {
                              \ifodd\i
                                  \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                              \else
                                  \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                              \\fi
                          }
                          \\node (outmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.25, minimum height="""+str(height)+"""mm*0.25] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1-""" + str(0.9/maps)+""")})+(start)$) {};
                          % \\node (inmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.15, minimum height="""+str(height)+"""mm*0.15] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1+""" + str(0.9/maps)+""")})+(start)$) {};
                          \\node (inmap"""+str(i)+""")[subfig] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1+""" + str(0.9/maps)+""")})+(start)$) {};
                        \end{scope}
                """
                else:
                    return r"""
                       \begin{scope}[xshift="""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)]
                          % \settowidth{\mytextlength}{$"""+map_info+"""$}
                           \coordinate (start) at (0,"""+str(pos)+"""mm);
                           \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                           \\foreach \i in {1,2,...,"""+str(maps)+"""}
                          {
                              \ifodd\i
                                  \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                              \else
                                  \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                              \\fi
                          }
                          \\node (outmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.25, minimum height="""+str(height)+"""mm*0.25] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1-""" + str(0.9/maps)+""")})+(start)$) {};
                          % \\node (inmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.15, minimum height="""+str(height)+"""mm*0.15] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1+""" + str(0.9/maps)+""")})+(start)$) {};
                        \end{scope}
                """
            else:
                if kernel_pre:
                    return r"""
                       \begin{scope}[xshift="""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)]
                          % \settowidth{\mytextlength}{$"""+map_info+"""$}
                           \coordinate (start) at (0,"""+str(pos)+"""mm);
                           \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                           \\foreach \i in {1,2,...,"""+str(maps)+"""}
                          {
                              \ifodd\i
                                  \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                              \else
                                  \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                              \\fi
                          }
                          % \\node (outmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.25, minimum height="""+str(height)+"""mm*0.25] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1-""" + str(0.9/maps)+""")})+(start)$) {};
                          % \\node (inmap"""+str(i)+""")[draw,fill=gray,subfig,minimum width="""+str(width)+"""mm*0.15, minimum height="""+str(height)+"""mm*0.15] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1+""" + str(0.9/maps)+""")})+(start)$) {};
                          \\node (inmap"""+str(i)+""")[subfig] at ($({("""+str(width)+"""mm/ 4*("""+str(maps)+"""-1)) / (1+"""+str(0.9/maps)+""")},{(-"""+str(height)+"""mm / 3*("""+str(maps)+"""-1)) / (1+""" + str(0.9/maps)+""")})+(start)$) {};
                        \end{scope}
                """
                else:
                    return r"""
               \begin{scope}[xshift="""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)]
                  % \settowidth{\mytextlength}{$"""+map_info+"""$}
                   \coordinate (start) at (0,"""+str(pos)+"""mm);
                   \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($(0,{"""+str(height)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
                   \\foreach \i in {1,2,...,"""+str(maps)+"""}
                  {
                      \ifodd\i
                          \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+ (start)$) {};
                      \else
                          \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(height)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(height)+"""mm/3*(\i-1)})+(start)$) {};
                      \\fi
                  }
                \end{scope}
                """

    else:
        pos = (height_pre-width)/2.
        height = height - 8
        return r"""
           \begin{scope}[xshift="""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)]
               \coordinate (start) at (0,"""+str(pos)+"""mm);
               \\node [subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(width)+"""mm] at ($(0,{"""+str(width)+"""mm/2+1.5em})+(start)$) {$"""+map_info+"""$};
               \\foreach \i in {1,2,...,"""+str(height)+"""}
              {
                  \ifodd\i
                      \\node [draw,fill=VegetaRed,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(width)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(width)+"""mm/3*(\i-1)})+ (start)$) {};
                  \else
                      \\node [draw,fill=VegetaGreen,subfig,minimum width="""+str(width)+"""mm, minimum height="""+str(width)+"""mm] at ($({"""+str(width)+"""mm/4*(\i-1)},{-"""+str(width)+"""mm/3*(\i-1)})+(start)$) {};
                  \\fi
              }
            \end{scope}
    """

def to_lines(i,all_kernel):
    if all_kernel[i+1] :
        return r"""
            \draw [line width=2pt](outmap"""+str(i)+""".south east) -- (inmap"""+str(i+1)+""".west);
            \draw [line width=2pt](outmap"""+str(i)+""".north east) -- (inmap"""+str(i+1)+""".west);
    """
    else:
        return r"""  """

def to_layers_info(i,layer_info_width,layer_info_heigth,layer_info):
    return r"""
           \node [subfig] at ($({"""+str(layer_info_width)+"""mm+"""+str(i)+"""*\layerSpace*(1-"""+str(i)+"""/40)},{"""+str(layer_info_heigth)+"""mm})$) {$"""+str(layer_info)+"""$};
"""

def to_end():
    return r"""
    \end{tikzpicture}
\end{document}
"""

def to_generate( arch, pathname="file.tex" ):
    with open(pathname, "w") as f:
        for c in arch:
            f.write( c )

if __name__ == '__main__':
    FILE = 'config.yaml'
    config = conf(FILE)
    print(config)
    filename = config['filename'] + '.tex'
    layers = config['layers']
    max_map_width = config[1]['width']
    layerSpace = config['layerSpace']
    if layerSpace == 'default':
        layerSpace = 127
    arch = []
    arch.append(to_head(layerSpace))
    arch.append(to_colors())
    arch.append(to_document())
    all_width = [0]
    all_height = [0]
    all_map = [0]
    all_layer_info = []
    all_kernel = [False]
    for i in range(layers):
        engine = config['engine']
        maps = config[i+1]['feature maps']
        width = config[i+1]['width']
        height = config[i+1]['height']
        kernel = config[i+1]['exist kernel']
        if maps != 1:
            j = i
            if maps <= 8:
                all_map.append(maps)
            elif maps <= 16:
                maps = 10
                all_map.append(maps)
            else:
                maps = maps / 2
                all_map.append(maps)
            # if width>63:
                # width = width / 8
                # height = height / 8
            # elif width < 33:
                # width = 8
                # height = 8
            if width<16:
                width = 12
                height = 12
        else:
            all_map.append(maps)
            j = 0
            if height>48:
                height = 24
            # if width>63:
                # width = width / 8
                # height = height / 8
            # elif width < 33:
                # width = 8
            if width<16:
                width = 8
        all_width.append(width)
        all_height.append(height)
        map_info = config[i+1]['maps information']
        layer_info = config[i+1]['layer information']
        all_layer_info.append(layer_info)
        arch.append(to_draw(i, maps, width, height, kernel, all_kernel[-1], all_height[-1-i], map_info, layer_info))
        print(kernel, all_kernel[-1])
        all_kernel.append(kernel)
        if j > 0:
            arch.append(to_lines(j-1,all_kernel))
    # max_height = max(all_height)
    N = layers+1
    all_sum_height = []
    all_sum_width = []
    for i in range(1,N):
        tmp = all_height[i]/3*(all_map[i]+1)
        all_sum_height.append(tmp)
        if all_map[i] != 1:
            tmp_width = all_width[i]/4*(all_map[i]-1)
            if len(all_sum_width)>0:
                if tmp_width < all_sum_width[-1] :
                    tmp_width = all_sum_width[-1] 
                    all_sum_width.append(tmp_width)
                else:
                    all_sum_width.append(tmp_width)
            else:
                all_sum_width.append(tmp_width)
        else:
            tmp_width = all_width[i]/4*(all_height[i]-1)
            if len(all_sum_width)>0:
                if tmp_width < all_sum_width[-1] :
                    tmp_width = all_sum_width[-1] 
                    all_sum_width.append(tmp_width)
                else:
                    all_sum_width.append(tmp_width)
            else:
                all_sum_width.append(tmp_width)
            # all_sum_width.append(all_width[i]/4*(all_height[i]-1))

    max_height = max(all_sum_height)
    max_index = all_sum_height.index(max_height)
    max_map_num = all_map[max_index+1]
    # print(max_map_num)
    # max_width = all_width[max_index+1]
    # layer_info_heigth = -max_height/3*(max_map_num+1)
    layer_info_heigth = -max_height
    # layer_info_width = max_width/4*(max_map_num-1)
    layer_info_width = all_sum_width
    for i in range(layers):
        arch.append(to_layers_info(i,layer_info_width[i],layer_info_heigth,all_layer_info[i]))

    arch.append(to_end())
    to_generate(arch, filename)
    command = engine + ' ' + filename
    os.system(command)

