# Brian Lesko 
# 6/5/2024

import numpy as np
from scipy import signal
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout='wide')

st.title('Control Systems Engineering - review material')

st.markdown('## LTI systems')

st.write('A linear time-invariant (LTI) approximates real world systems very well. It has two properties. An LTI system is Linear, which means that its outputs for a linear combination of inputs are the same as a linear combination of individual responses to those inputs. An LTI system is also Time-invariant. This means that the systems output does not depend on when an input was applied.')

st.markdown('### Transfer Function')
st.write(
    "A transfer function is defined as the ratio of the Laplace transform of the output "
    "to the input of a system, assuming zero initial conditions. It characterizes the system's behavior, "
    "independent of the input signal, by transforming the system's differential equation into a polynomial ratio in the Laplace variable \(s\)."
)
st.markdown('### Laplace Transform')
st.write(
    "The Laplace transform converts a time-domain function \(f(t)\) into its s-domain representation \(F(s)\), defined by:"
)
st.latex(r'\mathcal{L}\{f(t)\} = \int_0^\infty f(t)e^{-st}dt')
st.write(
    "This transformation simplifies differential equations to algebraic ones, facilitating easier analysis and solution of the system."
)


'---'

st.markdown('### First order systsem')

if st.radio('Stability', ['Stable', 'Unstable']) == 'Stable':
    sliders=[1,1,1]
else:
    sliders=[1,1,-1]

Function = st.empty()

col1, col2, col3, col4 = st.columns([1,1,5,1])


with col1: 
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    n = st.slider('Numerator', min_value=-1, max_value=10, value=sliders[0])
    d1 = st.slider('Denominator', min_value=-1, max_value=10, value=sliders[1])
    d2 = st.slider('Denominator 2', min_value=-1, max_value=10, value=sliders[2])

# Transfer function
num = [n]
den = [d1, d2]
sys = signal.TransferFunction(num, den)

# write the transfer function 
with Function: st.latex(fr'Y(s) = \frac{{{n}}}{{{d1}s + {d2}}}')

# Time vector
t = np.linspace(0, 10, 500)

# Step response
t, y = signal.step(sys, T=t)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='Step Response'))
fig.update_layout(title='Step Response', xaxis_title='Time', yaxis_title='Amplitude')

col3.plotly_chart(fig)

'---'

st.markdown('### Second order system')

if st.radio('Stability ', ['Stable', 'Unstable']) == 'Stable':
    sliders=[1,1,1,10]
else:
    sliders=[1,1,1,-1]

Function = st.empty()

col1, col2, col3, col4 = st.columns([1,1,5,1])

with col1:
    st.write('')
    st.write('')
    st.write('')
    n = st.slider('Numerator ', min_value=0, max_value=10, value=sliders[0])
    d1 = st.slider('Denominator 1 ', min_value=0, max_value=10, value=sliders[1])
    d2 = st.slider('Denominator 2 ', min_value=0, max_value=10, value=sliders[2])
    d3 = st.slider('Denominator 3 ', min_value=0, max_value=10, value=sliders[3])

# Transfer function
num = [n]
den = [d1, d2, d3]
sys = signal.TransferFunction(num, den)

# write the transfer function
with Function: st.latex(fr'Y(s) = \frac{{{n}}}{{{d1}s^2 + {d2}s + {d3}}}')

# Time vector
t = np.linspace(0, 10, 500)

# Step response
t, y = signal.step(sys, T=t)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='Step Response'))
fig.update_layout(title='Step Response', xaxis_title='Time', yaxis_title='Amplitude')

col3.plotly_chart(fig)

'---'

st.markdown('### Third order system')

if st.radio('Stability  ', ['Stable', 'Unstable']) == 'Stable':
    sliders=[1,1,6,10,6]
else:
    sliders=[1,1,1,-1,1]

Function = st.empty()

col1, col2, col3, col4 = st.columns([1,1,5,1])

with col1:
    n = st.slider('Numerator  ', min_value=0, max_value=10, value=sliders[0])
    d1 = st.slider('Denominator 1  ', min_value=0, max_value=10, value=sliders[1])
    d2 = st.slider('Denominator 2  ', min_value=0, max_value=10, value=sliders[2])
    d3 = st.slider('Denominator 3  ', min_value=0, max_value=10, value=sliders[3])
    d4 = st.slider('Denominator 4  ', min_value=0, max_value=10, value=sliders[4])

# Transfer function
num = [n]
den = [d1, d2, d3, d4]
sys = signal.TransferFunction(num, den)

# write the transfer function
with Function: st.latex(fr'Y(s) = \frac{{{n}}}{{{d1}s^3 + {d2}s^2 + {d3}s + {d4}}}')

# Time vector
t = np.linspace(0, 10, 500)

# Step response
t, y = signal.step(sys, T=t)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='Step Response'))
fig.update_layout(title='Step Response', xaxis_title='Time', yaxis_title='Amplitude')

col3.plotly_chart(fig)

'---'