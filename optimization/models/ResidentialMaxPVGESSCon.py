from pyomo.core import *
import pyomo.environ

class Model:
	model = AbstractModel()
	
	
	model.T = Set()  # Index Set for time steps of optimization horizon
	model.T_SoC = Set()  # SoC of the ESSs at the end of optimization horizon are also taken into account
	
	##################################       PARAMETERS            #################################
	################################################################################################
	
	model.dT = Param(within=PositiveIntegers)  # Number of seconds in one time step
	
	# model.Price_Forecast=Param(model.T)                             #Electric price forecast
	
	# definition of the energy storage system
	model.ESS_Min_SoC = Param(within=NonNegativeReals)  # Minimum SoC of ESSs
	model.ESS_Max_SoC = Param(within=PositiveReals)  # Maximum SoC of ESSs
	model.SoC_Value = Param(within=PositiveReals)
	model.ESS_Capacity = Param(within=PositiveReals)  # Storage Capacity of ESSs
	model.ESS_Max_Charge_Power = Param(within=PositiveReals)  # Max Charge Power of ESSs
	model.ESS_Max_Discharge_Power = Param(within=PositiveReals)  # Max Discharge Power of ESSs
	model.ESS_Charging_Eff = Param(within=PositiveReals)  # Charging efficiency of ESSs
	model.ESS_Discharging_Eff = Param(within=PositiveReals)  # Discharging efficiency of ESSs
	
	#definition of the grid maximal power
	model.P_Grid_Max_Export_Power = Param(within=NonNegativeReals)  # Max active power export
	model.Q_Grid_Max_Export_Power = Param(within=NonNegativeReals)  # Max reactive power export
	
	#definition of the PV
	model.P_PV = Param(model.T, within=NonNegativeReals)  # PV PMPP forecast
	model.PV_Inv_Max_Power = Param(within=PositiveReals)  # PV inverter capacity
	
	#definition of the load
	model.P_Load = Param(model.T, within=NonNegativeReals)  # Active power demand

	model.GlobalTargetWeight = Param(within=NonNegativeReals)
	model.LocalTargetWeight = Param(within=NonNegativeReals)

	model.ESS_Control = Param(model.T, within=Reals)  # TODO: define domain
	
	
	################################################################################################
	
	##################################       VARIABLES             #################################
	################################################################################################

	model.P_Grid_Output = Var(model.T, within=Reals)
	#model.P_Grid_Output = Var(model.T, within=Reals, bounds=(-model.P_Grid_Max_Export_Power, 0))
	model.P_PV_Output = Var(model.T, within=NonNegativeReals, bounds=(0, model.PV_Inv_Max_Power))  # initialize=iniVal)
	model.P_ESS_Output = Var(model.T, within=Reals, bounds=(-model.ESS_Max_Charge_Power, model.ESS_Max_Discharge_Power))  # ,initialize=iniSoC)
	model.SoC_ESS = Var(model.T_SoC, within=NonNegativeReals, bounds=(model.ESS_Min_SoC, model.ESS_Max_SoC))
	model.Deviation = Var(model.T, within=Reals)

	################################################################################################

	###########################################################################
	#######                         CONSTRAINTS                         #######

	#rule to limit the PV ouput to value of the PV forecast
	def con_rule_pv_potential(model, t):
	    return model.P_PV_Output[t]  <= model.P_PV[t]

	#rule for setting the maximum export power to the grid
	def con_rule_grid_output_power(model, t):
		return model.P_Grid_Output[t] >= -model.P_Grid_Max_Export_Power

	# ESS SoC balance
	def con_rule_socBalance(model, t):
	    return model.SoC_ESS[t + 1] == model.SoC_ESS[t] - model.P_ESS_Output[t] * model.dT / model.ESS_Capacity / 3600

	#initialization of the first SoC value to the value entered through the API
	def con_rule_iniSoC(model):
		if model.SoC_Value > model.ESS_Max_SoC:
			model.SoC_Value = model.ESS_Max_SoC
			return model.SoC_ESS[0] == model.SoC_Value
		elif model.SoC_Value < model.ESS_Min_SoC:
			model.SoC_Value = model.ESS_Min_SoC
			return model.SoC_ESS[0] == model.SoC_Value
		else:
			return model.SoC_ESS[0] == model.SoC_Value

	#Definition of the energy balance in the system
	def con_rule_energy_balance(model,t):
	    return model.P_Load[t] == model.P_PV_Output[t] + model.P_ESS_Output[t] + model.P_Grid_Output[t]

	def con_rule_deviation(model, t):
		return model.Deviation[t] == model.P_ESS_Output[t] - model.ESS_Control[t]

	model.con_pv_max = Constraint(model.T, rule = con_rule_pv_potential)
	model.conn_grid_output_max = Constraint(model.T, rule = con_rule_grid_output_power)
	model.con_ess_soc = Constraint(model.T, rule=con_rule_socBalance)
	model.con_ess_Inisoc = Constraint(rule=con_rule_iniSoC)
	model.con_energy_balance = Constraint(model.T, rule=con_rule_energy_balance)
	model.con_deviation = Constraint(model.T, rule=con_rule_deviation)

	###########################################################################
	#######                         OBJECTIVE                           #######
	###########################################################################
	def obj_rule(model):
	    return sum(model.LocalTargetWeight*(model.P_PV[t]-model.P_PV_Output[t])*(model.P_PV[t]-model.P_PV_Output[t])
                       +model.GlobalTargetWeight*model.Deviation[t]*model.Deviation[t]
                       for t in model.T)
	
	model.obj = Objective(rule=obj_rule, sense=minimize)
