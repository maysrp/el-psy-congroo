from machine import I2C, Pin
from showStf import stfe
import tca9548a_test
import time

tca=tca9548a_test.TCA9548A(0x70,19,18,20000000)

st=stfe(tca)
st.showAll('123123')
st.showStr(0,1)
st.showFull(2,1)
st.showAll('')
st.showAll('ACFUN')