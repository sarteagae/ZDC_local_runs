#!/usr/bin/env python3
import ROOT
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str,
                    help="File you want to plot")

args = parser.parse_args()
filename = str(args.file)
print('Opening: ',filename)
root_file = ROOT.TFile.Open(filename, 'read')

##### ZCZ - ######################################
c1 = ROOT.TCanvas()
c1.Divide(4,4)
p1 =  c1.cd(1)
h1 = root_file.Get('zdcana/ADC/hZDCM_EM0')
h1.SetStats(0)
p1.SetLogy()
#y1 = p1.GetYaxis()
#p1.SetLabelFontYaxis(43)
h1.Draw('colz')

p2 = c1.cd(2)
h2 = root_file.Get('zdcana/ADC/hZDCM_EM1')
h2.SetStats(0)
p2.SetLogy()
h2.Draw('colz')

p3 = c1.cd(3)
h3 = root_file.Get('zdcana/ADC/hZDCM_EM2')
h3.SetStats(0)
p3.SetLogy()
h3.Draw('colz')

p4 = c1.cd(4)
h4 = root_file.Get('zdcana/ADC/hZDCM_EM3')
h4.SetStats(0)
p4.SetLogy()
h4.Draw('colz')

p5 = c1.cd(5)
h5 = root_file.Get('zdcana/ADC/hZDCM_EM4')
h5.SetStats(0)
p5.SetLogy()
h5.Draw('colz')

p6 = c1.cd(6)
h6 = root_file.Get('zdcana/ADC/hZDCM_EM5')
h6.SetStats(0)
p6.SetLogy()
h6.Draw('colz')

p7 = c1.cd(7)
h7 = root_file.Get('zdcana/ADC/hZDCM_EM6')
h7.SetStats(0)
p7.SetLogy()
h7.Draw('colz')

p8 = c1.cd(8)
h8 = root_file.Get('zdcana/ADC/hZDCM_EM7')
h8.SetStats(0)
p8.SetLogy()
h8.Draw('colz')

p9 = c1.cd(9)
h9 = root_file.Get('zdcana/ADC/hZDCM_EM8')
h9.SetStats(0)
p9.SetLogy()
h9.Draw('colz')

p10 = c1.cd(10)
h10 = root_file.Get('zdcana/ADC/hZDCM_EM19')
h10.SetStats(0)
p10.SetLogy()
h10.Draw('colz')

p11 = c1.cd(11)
h11 = root_file.Get('zdcana/ADC/hZDCM_EM10')
h11.SetStats(0)
p11.SetLogy()
h11.Draw('colz')

p12 = c1.cd(12)
h12 = root_file.Get('zdcana/ADC/hZDCM_EM11')
h12.SetStats(0)
p12.SetLogy()
h12.Draw('colz')

p13 = c1.cd(13)
h13 = root_file.Get('zdcana/ADC/hZDCM_EM12')
h13.SetStats(0)
p13.SetLogy()
h13.Draw('colz')

p14 = c1.cd(14)
h14 = root_file.Get('zdcana/ADC/hZDCM_EM13')
h14.SetStats(0)
p14.SetLogy()
h14.Draw('colz')

p15 = c1.cd(15)
h15 = root_file.Get('zdcana/ADC/hZDCM_EM14')
h15.SetStats(0)
p15.SetLogy()
h15.Draw('colz')

p16 = c1.cd(16)
h16 = root_file.Get('zdcana/ADC/hZDCM_EM15')
h16.SetStats(0)
p16.SetLogy()
h16.Draw('colz')

#**********************************ZDCM_HAD
c2 = ROOT.TCanvas()
c2.Divide(4,4)
p17 =  c2.cd(1)
h17 = root_file.Get('zdcana/ADC/hZDCM_HAD0')
h17.SetStats(0)
p17.SetLogy()
#y1 = p19.GetYaxis()
#p19.SetLabelFontYaxis(43)
h17.Draw('colz')

p18 = c2.cd(2)
h18 = root_file.Get('zdcana/ADC/hZDCM_HAD1')
h18.SetStats(0)
p18.SetLogy()
h18.Draw('colz')

p19 = c2.cd(3)
h19 = root_file.Get('zdcana/ADC/hZDCM_HAD2')
h19.SetStats(0)
p19.SetLogy()
h19.Draw('colz')

p20 = c2.cd(4)
h20 = root_file.Get('zdcana/ADC/hZDCM_HAD3')
h20.SetStats(0)
p20.SetLogy()
h20.Draw('colz')

p21 = c2.cd(5)
h21 = root_file.Get('zdcana/ADC/hZDCM_HAD4')
h21.SetStats(0)
p21.SetLogy()
h21.Draw('colz')

p22 = c2.cd(6)
h22 = root_file.Get('zdcana/ADC/hZDCM_HAD5')
h22.SetStats(0)
p22.SetLogy()
h22.Draw('colz')

p23 = c2.cd(7)
h23 = root_file.Get('zdcana/ADC/hZDCM_HAD6')
h23.SetStats(0)
p23.SetLogy()
h23.Draw('colz')

p24 = c2.cd(8)
h24 = root_file.Get('zdcana/ADC/hZDCM_HAD7')
h24.SetStats(0)
p24.SetLogy()
h24.Draw('colz')

p25 = c2.cd(9)
h25 = root_file.Get('zdcana/ADC/hZDCM_HAD8')
h25.SetStats(0)
p25.SetLogy()
h25.Draw('colz')

p26 = c2.cd(10)
h26 = root_file.Get('zdcana/ADC/hZDCM_HAD19')
h26.SetStats(0)
p26.SetLogy()
h26.Draw('colz')

p27 = c2.cd(11)
h27 = root_file.Get('zdcana/ADC/hZDCM_HAD10')
h27.SetStats(0)
p27.SetLogy()
h27.Draw('colz')

p28 = c2.cd(12)
h28 = root_file.Get('zdcana/ADC/hZDCM_HAD11')
h28.SetStats(0)
p28.SetLogy()
h28.Draw('colz')

p29 = c2.cd(13)
h29 = root_file.Get('zdcana/ADC/hZDCM_HAD12')
h29.SetStats(0)
p29.SetLogy()
h29.Draw('colz')

p30 = c2.cd(14)
h30 = root_file.Get('zdcana/ADC/hZDCM_HAD13')
h30.SetStats(0)
p30.SetLogy()
h30.Draw('colz')

p31 = c2.cd(15)
h31 = root_file.Get('zdcana/ADC/hZDCM_HAD14')
h31.SetStats(0)
p31.SetLogy()
h31.Draw('colz')

p32 = c2.cd(16)
h32 = root_file.Get('zdcana/ADC/hZDCM_HAD15')
h32.SetStats(0)
p32.SetLogy()
h32.Draw('colz')


#**********************************ZDCM_RPD
c3 = ROOT.TCanvas()
c3.Divide(4,4)
p33 =  c3.cd(1)
h33 = root_file.Get('zdcana/ADC/hZDCM_RPD0')
h33.SetStats(0)
p33.SetLogy()
#y1 = p35.GetYaxis()
#p35.SetLabelFontYaxis(43)
h33.Draw('colz')

p34 = c3.cd(2)
h34 = root_file.Get('zdcana/ADC/hZDCM_RPD1')
h34.SetStats(0)
p34.SetLogy()
h34.Draw('colz')

p35 = c3.cd(3)
h35 = root_file.Get('zdcana/ADC/hZDCM_RPD2')
h35.SetStats(0)
p35.SetLogy()
h35.Draw('colz')

p36 = c3.cd(4)
h36 = root_file.Get('zdcana/ADC/hZDCM_RPD3')
h36.SetStats(0)
p35.SetLogy()
h36.Draw('colz')

p37 = c3.cd(5)
h37 = root_file.Get('zdcana/ADC/hZDCM_RPD4')
h37.SetStats(0)
p37.SetLogy()
h37.Draw('colz')

p38 = c3.cd(6)
h38 = root_file.Get('zdcana/ADC/hZDCM_RPD5')
h38.SetStats(0)
p38.SetLogy()
h38.Draw('colz')

p39 = c3.cd(7)
h39 = root_file.Get('zdcana/ADC/hZDCM_RPD6')
h39.SetStats(0)
p39.SetLogy()
h39.Draw('colz')

p40 = c3.cd(8)
h40 = root_file.Get('zdcana/ADC/hZDCM_RPD7')
h40.SetStats(0)
p40.SetLogy()
h40.Draw('colz')

p41 = c3.cd(9)
h41 = root_file.Get('zdcana/ADC/hZDCM_RPD8')
h41.SetStats(0)
p41.SetLogy()
h41.Draw('colz')

p42 = c3.cd(10)
h42 = root_file.Get('zdcana/ADC/hZDCM_RPD19')
h42.SetStats(0)
p42.SetLogy()
h42.Draw('colz')

p43 = c3.cd(11)
h43 = root_file.Get('zdcana/ADC/hZDCM_RPD10')
h43.SetStats(0)
p43.SetLogy()
h43.Draw('colz')

p44 = c3.cd(12)
h44 = root_file.Get('zdcana/ADC/hZDCM_RPD11')
h44.SetStats(0)
p44.SetLogy()
h44.Draw('colz')

p45 = c3.cd(13)
h45 = root_file.Get('zdcana/ADC/hZDCM_RPD12')
h45.SetStats(0)
p45.SetLogy()
h45.Draw('colz')

p46 = c3.cd(14)
h46 = root_file.Get('zdcana/ADC/hZDCM_RPD13')
h46.SetStats(0)
p46.SetLogy()
h46.Draw('colz')

p47 = c3.cd(15)
h47 = root_file.Get('zdcana/ADC/hZDCM_RPD14')
h47.SetStats(0)
p47.SetLogy()
h47.Draw('colz')

p48 = c3.cd(16)
h48 = root_file.Get('zdcana/ADC/hZDCM_RPD15')
h48.SetStats(0)
p48.SetLogy()
h48.Draw('colz')


c1.SaveAs(filename.replace(".root","")+'_EM_minus.pdf')
c2.SaveAs(filename.replace(".root","")+'_HAD_minus.pdf')
c3.SaveAs(filename.replace(".root","")+'_RPD_minus.pdf')