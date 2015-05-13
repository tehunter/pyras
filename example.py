# -*- coding: utf-8 -*-
"""

"""
import datetime as dt 

from pyras.controllers import RAS500, RAS41, kill_ras
from pyras.controllers.hecras import ras_constants as RC

#project = r'temp_examples\Steady Examples\BEAVCREK.prj'
#project = r'D:\Users\penac1\Dropbox (Personal)\it\repos\git\pyras\temp_examples\Steady Examples\BEAVCREK.prj'
#project = r'temp_examples\Unsteady Examples\NavigationDam\ROCK_TEST.prj'

#project = r'D:\Users\penac1\Dropbox (Personal)\it\repos\git\pyras\temp\Unsteady Examples\BEAV_STO_PROBLEM.prj'
project = r'D:\Users\penac1\Dropbox (Personal)\it\repos\git\pyras\temp_examples\Unsteady Examples\BaldLatWeir.prj'

#with RAS500(project) as rc:
#    res = rc.Project_Current()
#    print(rc.version())
#    print('Project_Current:')
#    print(res)
#    print('')
#    for m in sorted(dir(rc)):
#        print(m)
#    rc.pause(10)

rc = RAS500()
rc.ShowRas()

# %% Project
rc.Project_Open(project)

#res = rc.Project_Current()
#print('Project_Current:')
#print(res)
#print('')

#rc.Compute_HideComputationWindow()
#rc.Compute_ShowComputationWindow()
#res = rc.Compute_CurrentPlan()
#print('Compute_CurrentPlan:')
#print(res)
#print('')

#res = rc.Compute_Cancel()
#print('\nCompute_Cancel', res)

#res = rc.Compute_Complete()
#print('Compute_Complete')
#print(res)
#print('')

# %% Curent (Controller Class)
#res = rc.CurrentGeomFile()
#print('CurrentGeomFile')
#print(res)
#print('')
#
#res = rc.CurrentPlanFile()
#print('CurrentPlanFile')
#print(res)
#print('')
#
#res = rc.CurrentProjectFile()
#print('CurrentProjectFile')
#print(res)
#print('')
#
#res = rc.CurrentProjectTitle()
#print('CurrentProjectTitle')
#print(res)
#print('')
#
#res = rc.CurrentSteadyFile()
#print('CurrentSteadyFile')
#print(res)
#print('')
#
#res = rc.CurrentUnSteadyFile()
#print('CurrentUnSteadyFile')
#print(res)
#print('')

# %% Geometry (Geometry Class)

#geo = rc.Geometry()
#
#res = geo.RiverIndex('Beaver Creek')
#print('RiverIndex')
#print(res)
#print('')
#
#res = geo.RiverName(1)
#print('RiverName')
#print(res)
#print('')
#
#res = geo.ReachName(1, 1)
#print('ReachName')
#print(res)
#print('')
#
#res = geo.ReachInvert_nPoints(1, 1)
#print('ReachInvert_nPoints')
#print(res)
#print('')
#
#res = geo.ReachInvert_Points(1, 1)
#print('ReachInvert_Points')
#print(res)
#print('')
#
#res = geo.ReachIndex(1, 'Kentwood')
#print('ReachIndex')
#print(res)
#print('')
#
#res = geo.nRiver()
#print('nRiver')
#print(res)
#print('')
#
#res = geo.nReach(1)
#print('nReach')
#print(res)
#print('')
#
#res = geo.NodeType(1, 1, 1)
#print('NodeType')
#print(res)
#print('')
#
#res = geo.NodeRS(1, 1, 1)
#print('NodeRS')
#print(res)
#print('')
#
#res = geo.NodeIndex(1, 1, '5.99')
#print('NodeIndex')
#print(res)
#print('')
#
#res = geo.NodeCutLine_Points(1, 1, 1)
#print('NodeCutLine_Points')
#print(res)
#print('')
#
#res = geo.NodeCutLine_nPoints(1, 1, 1)
#print('NodeCutLine_nPoints')
#print(res)
#print('')
#
#res = geo.NodeCType(1, 1, 8)
#print('NodeCType')
#print(res)
#print('')

#%% Edit Add (Controller Class)
#res = rc.Edit_AddBC('Beaver Creek', 'Kentwood', '5.691')
#print('Edit_AddBC')
#print(res)
#print('')
#
#res = rc.Edit_AddIW('Beaver Creek', 'Kentwood', '5.692')
#print('Edit_AddIW')
#print(res)
#print('')
#
#res = rc.Edit_AddLW('Beaver Creek', 'Kentwood', '5.693')
#print('Edit_AddLW')
#print(res)
#print('')
#
#res = rc.Edit_AddXS('Beaver Creek', 'Kentwood', '5.694')
#print('Edit_AddXS')
#print(res)
#print('')

# %% Edit (Controller Class)

#rc.Edit_BC('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_BC')
#print('')
#
#rc.Edit_GeometricData()
#print('Edit_GeometricData')
#print('')
#
#rc.Edit_IW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_IW')
#print('')
#
#rc.Edit_LW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_LW')
#print('')
#
#rc.Edit_MultipleRun()
#print('Edit_MultipleRun')
#print('')
#
#rc.Edit_PlanData()
#print('Edit_PlanData')
#print('')
#
#rc.Edit_QuasiUnsteadyFlowData()
#print('Edit_QuasiUnsteadyFlowData')
#print('')
#
#rc.Edit_SedimentData()
#print('Edit_SedimentData')
#print('')
#
#rc.Edit_SteadyFlowData()
#print('Edit_SteadyFlowData')
#print('')
#
#rc.Edit_UnsteadyFlowData()
#print('Edit_UnsteadyFlowData')
#print('')
#
#rc.Edit_WaterQualityData()
#print('Edit_WaterQualityData')
#print('')
#
#rc.Edit_XS('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_XS')
#print('')

# %% Geometry (Controller Class)
#res = rc.ExportGIS()
#print('ExportGIS')
#print(res)
#print('')

# %% Geometry (Controller Class)

# Not tested
#res = rc.Geometery_GISImport(self, title, Filename)
#print('Geometery_GISImport')
#print(res)
#print('')

# Not tested but seems to work
#res = rc.Geometry_GetGateNames(1, 1, '5.39')
#print('Geometry_GetGateNames')
#print(res)
#print('')

# Not working
#res = rc.Geometry_GetGML('Bvr.Cr.+Bridge - P/W: New Le, Lc')
#print('Geometry_GetGML')
#print(res)
#print('')

#res = rc.Geometry_GetNode(1, 1, '5.39')
#print('Geometry_GetNode')
#print(res)
#print('')
#
#res = rc.Geometry_GetNodes(1, 1)
#print('Geometry_GetNodes')
#print(res)
#print('')
#
#res = rc.Geometry_GetReaches(1)
#print('Geometry_GetReaches')
#print(res)
#print('')
#
#res = rc.Geometry_GetRivers()
#print('Geometry_GetRivers')
#print(res)
#print('')
#
#res = rc.Geometry_SetMann('Beaver Creek', 'Kentwood', '5.99',
#                          3, (0.12, 0.13, 0.14), (5, 36, 131))
#print('Geometry_SetMann')
#print(res)
#print('')
#
#res = rc.Geometry_SetMann_LChR('Beaver Creek', 'Kentwood', '5.99', 0.15, 0.10,
#                               0.16)
#print('Geometry_SetMann_LChR')
#print(res)
#print('')
#
#res = rc.Geometry_SetSAArea('test', 1200)
#print('Geometry_SetSAArea')
#print(res)
#print('')

# %% Get (Controller Class)
#res = rc.GetRASVersion()
#print('GetRASVersion')
#print(res)
#print('')
#
#res = rc.HECRASVersion()
#print('HECRASVersion', res)
#print(res)
#print('')

# %% Output 
#river = 1
#reach = 1
#n = 1
#station = '135068.7'

#res = rc.Output_ComputationLevel_Export('export_test2.txt')
#print('Output_ComputationLevel_Export', res)
#print('')
#
#res = rc.Output_GetNode(river, reach, station)
#print('Output_GetNode', res)
#print('')
#
#res = rc.Output_GetNodes(river, reach)
#print('Output_GetNodes', res)
#print('')

#res = rc.Output_GetProfiles()
#print('Output_GetProfiles', res)
#print('')

#reach = 'Loc Hav'
#res = rc.Output_GetReach(river, reach)
#print('Output_GetReach', res)
#print('')

#res = rc.Output_GetReaches(river)
#print('Output_GetReaches', res)
#print('')

#river_name = 'Bald Eagle'
#res = rc.Output_GetRiver(river_name)
#print('Output_GetRiver', res)
#print('')

#res = rc.Output_GetRivers()
#print('Output_GetRivers', res)
#print('')

#updn = 0
#prof = 1
#nVar = RC.WS_ELEVATION
#res = rc.Output_NodeOutput(river, reach, n, updn, prof, nVar)
#print('Output_NodeOutput', res)
#print('')

#riv_id = 1
#rch = 1
#prof = 1
#nVar = RC.PROFILE
#res = rc.Output_ReachOutput(riv_id, rch, prof, nVar)
#print('Output_ReachOutput', res)
#print('')

#res = rc.Output_Variables()
#print('Output_Variables', res)
#print('')

#riv = 1
#rch = 1
#n = 1
#updn = 1
#prof = 1
#res = rc.Output_VelDist(riv, rch, n, updn, prof)
#print('Output_Output_VelDist', res)
#print('')

#riv = 'Bald Eagle'
#rch = 'Loc Hav'
#rs = '138154.4'
#res = rc.OutputDSS_GetStageFlow(riv, rch, rs)
#print('OutputDSS_GetStageFlow', res)
#print('')

#res = rc.OutputDSS_GetStageFlowSA('Lower SA')
#print('OutputDSS_GetStageFlowSA', res)
#print('')

# %% Plan
#plan = 'Unsteady with Bridges, Dam, later weirs/'
#res = rc.Plan_GetFilename(plan)
#print('Plan_GetFilename', res)
#print('')

#res = rc.Plan_Names(False)
#print('Plan_Names', res)
#print('')

#res = rc.Plan_Reports()
#print('Plan_Reports', res)
#print('')

#plan = 'Unsteady with Bridges, Dam, later weirs/'
#res = rc.Plan_SetCurrent(plan)
#print('Plan_SetCurrent', res)
#print('')

#plan = 'Unsteady with Bridges, Dam, later weirs/'
#show_message = False
#res = rc.PlanOutput_IsCurrent(plan, show_message)
#print('PlanOutput_IsCurrent', res)
#print('')



# %% Plot

#rc.PlotHydraulicTables('Beaver Creek', 'Kentwood', '5.99')
#print('PlotHydraulicTables', res)
#print('')

# %% Schematic (Controller Class)
#res = rc.Schematic_ReachCount()
#print('Schematic_ReachCount')
#print(res)
#print('')
#
#res = rc.Schematic_ReachPointCount()
#print('Schematic_ReachPointCount')
#print(res)
#print('')
#
#res = rc.Schematic_ReachPoints()
#print('Schematic_ReachPoints')
#print(res)
#print('')
#
#res = rc.Schematic_XSCount()
#print('Schematic_XSCount')
#print(res)
#print('')
#
#res = rc.Schematic_XSPointCount()
#print('Schematic_XSPointCount')
#print(res)
#print('')
#
#res = rc.Schematic_XSPoints()
#print('Schematic_XSPointCount')
#print(res)
#print('')

rc.close()
kill_ras()
