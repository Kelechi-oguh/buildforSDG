def estimator(data):
  cases_reported = data["reportedCases"]
  days = Estimation_Period()
  Output_dict = {}

  Output_dict["Data"] = data
  Output_dict["Impact"] = Impact(cases_reported, days)
  Output_dict["SevereImpact"] = SevereImpact(cases_reported, days)
  return Output_dict

def Estimation_Period():
  period = input("Select Estimation Unit (type: days, weeks or months): ").lower()
  
  while period not in ["days", "weeks", "months"]:
    period = input("""WRONG INPUT!!
    Please Enter a valid estimation unit(days, weeks or months): """).lower()

  number = int(input("""Enter the number for the unit selected above 
  (ENTER WHOLE NUMBER ONLY e.g 12): """))

  num_of_days = 0
  if period == "days":
    num_of_days = number
  elif period == "weeks":
    num_of_days = number * 7
  elif period == "months":
    num_of_days = number * 30

  return num_of_days 


def Impact(cases_reported, days):
  currentlyInfected = cases_reported * 10
  infectionsByRequestTime = currentlyInfected * (2 ** (days//3))
  impact_dict = {}

  impact_dict["currentlyInfected"] = currentlyInfected
  impact_dict["infectionsByRequestTime"] = infectionsByRequestTime
  return impact_dict

def SevereImpact(cases_reported, days):
  currentlyInfected = cases_reported * 50
  infectionsByRequestTime = currentlyInfected * (2 ** (days//3))
  SevereImpact_dict = {}

  SevereImpact_dict["currentlyInfected"] = currentlyInfected
  SevereImpact_dict["infectionsByRequestTime"] = infectionsByRequestTime
  return SevereImpact_dict


the_input = {
          "region": {
          "name": "Africa",
          "avgAge": 19.7,
          "avgDailyIncomeInUSD": 5,
          "avgDailyIncomePopulation": 0.71
          },
          "periodType": "days",
          "timeToElapse": 58,
          "reportedCases": 674,
          "population": 66622705,
          "totalHospitalBeds": 1380614
           }

print(estimator(the_input))