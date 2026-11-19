higgs4l_br = {
'124.8_2e2mu' : .0000582,
'124.9_emutau' : .000274,
'124.9_4e' : .0000324,
'124.9_4mu' : .0000324,
'124.9_2e2mu' : .0000588,
'125.0_4e' : .00003254,
'125.0_4mu' : .00003254,
'125.0_2e2mu' : .00005897,
'125.0_emutau' : .0002745,
'125.09_4e' : .00003280,
'125.09_4mu' : .00003280,
'125.09_2e2mu' : .00005947,
'125.09_emutau' : .0002768,
'125.1_4e' : .0000330,
'125.1_4mu' : .0000330,
'125.1_2e2mu' : .0000599,
'125.2_4e' : .0000333,
'125.2_4mu' : .0000333,
'125.2_2e2mu' : .0000604,
# NOTE for the Hgg + H4l combination (to be discussed): the combination fits run at mH = 125.07 GeV, while the
# SM reference used so far is read at mH = 125.38 GeV. BR(H->4l), 4e + 4mu + 2e2mu: 1.283e-4 at 125.38 GeV and
# 1.248e-4 at 125.07 GeV, which is 2.7% lower. Hgg evaluates BR(H->gamma gamma) at the fit mass, where it is flat
# (2.270e-3 from 125.0 to 125.4 GeV). The reference is chosen with sm_reference_136TeV below.
# 125.07: linear interpolation between the 125.0 and 125.09 entries above (weight 7/9 on 125.09)
'125.07_4e' : .0000327422,
'125.07_4mu' : .0000327422,
'125.07_2e2mu' : .0000593589,
# Extrapolated from YR values with pol2 fit
'125.38_4e' : .00003364,
'125.38_4mu' : .00003364,
'125.38_2e2mu' : .000061048,

}

higgsZZ_br = {
'125.0': 0.02619,
'125.09': 0.02641,
}

filtereff = {
'WH': 0.010384,
'ZH': 0.028544,
'ttH': 0.029658
}

# YR 4
higgs_xs = {
'ggH_125.0' : 48580, # N3LO
'VBF_125.0' : 3782,
'WH_125.0' : 1373.0,
'ZH_125.0' : 883.9,
'ttH_125.0' : 507.1,
'ggH_125.09' : 48520, # N3LO
'VBF_125.09' : 3779,
'WH_125.09' : 1369.0,
'ZH_125.09' : 882.4,
'ttH_125.09' : 506.5,
# Extrapolated from YR values with pol2 fit
'ggH_125.38' : 48314, # N3LO
'VBF_125.38' : 3771,
'WH_125.38' : 1359.0,
'ZH_125.38' : 876.7,
'ttH_125.38' : 503.3,
}

# Taken from : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG136TeVxsec_extrap
higgs_xs_136TeV = {
'ggH_125.0':  52230,
'VBF_125.0': 4078,
'WH_125.0': 1457,
'ZH_125.0': 943.9,
'ttH_125.0': 570.0,
'ggH_125.38' : 51960, # N3LO
'VBF_125.38' : 4067,
'WH_125.38' : 1442.0,
'ZH_125.38' : 936.1,
'ttH_125.38' : 563.8,
}

# LHCHWG Report 5 (R5 v1.1.3, https://gitlab.cern.ch/LHCHIGGSXS/LHCHXSWG1/crosssections), 13.6 TeV, in fb.
# Linear interpolation between the R5 points at 125.0 and 125.09 GeV (weight 7/9 on 125.09), six significant digits.
higgs_xs_136TeV_R5 = {
'ggH_125.07' : 51673.3, # N3LO
'VBF_125.07' : 4109.77,
'WH_125.07' : 1465.10,
'ZH_125.07' : 947.206,
'ttH_125.07' : 592.189,
}

# SM reference of the 13.6 TeV signal model in fit/createXSworkspace.py: the cross-section table and the mass point.
# The branching fractions are read from higgs4l_br at the same mass (YR4 values).
sm_reference_136TeV = {
'YR4_125.38' : {'xs': higgs_xs_136TeV, 'mass': '125.38'}, # as used so far
'R5_125.07' : {'xs': higgs_xs_136TeV_R5, 'mass': '125.07'},
}
# Reference used unless the environment variable H4L_SM_REFERENCE names another entry of sm_reference_136TeV
sm_reference_136TeV_default = 'YR4_125.38'

# TODO: Update to Run3 values
unc_qcd = {
    'VBF_125.38' : 0.002,
    'WH_125.38' : 0.01,
    'ZH_125.38' : 0.031,
    'ttH_125.38': 0.0655
}
unc_pdf = {
    'VBF_125.38' : 0.021,
    'WH_125.38' : 0.023,
    'ZH_125.38' : 0.025,
    'ttH_125.38': 0.081
}
unc_acc = 0.02
unc_br = 0.02
