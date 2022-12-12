leaguesLabel = {
    'L1':5, 'DFB':5, 'DFL':4, 'NL1':3, 'NLP':3, 'ES1':5, 'CDR':5, 'PO1':4, 'POCP':4, 'FR1':5, 'GB1':5, 'CGB':5, 'IT1':5,
    'CIT':5, 'CL':5, 'EL':4, 'BE1':3, 'BESC':3, 'RU1':3, 'RUP':3, 'UKR1':3, 'UKRP':3, 'TR1':3
}


def get_appearances_required():
  fileAppearances = "dataset/appearances.csv"
  dataRawAppearances = open(fileAppearances, "r").readlines()
  dataAppearances = []
  exploitableData = []
  
  for line in dataRawAppearances :
    dataAppearances.append(line.split(','))
  dataAppearances = dataAppearances[1:]
  
  for app in dataAppearances:
    if("2019" in app[4] or "2020" in app[4] or "2021" in app[4] or "2022" in app[4]):
      exploitableData.append(app)
      
  newData = []
  for data in exploitableData:
    if( "L1" == data[6] or "DFB" == data[6] or "DFL" == data[6] or "NL1" == data[6] or "NLP" == data[6] or "ES1" == data[6] or "CDR" == data[6] or "PO1" == data[6] or "POCP" == data[6] or "FR1" == data[6] or "GB1" == data[6] or "CGB" == data[6] or "IT1" == data[6] or "CIT" == data[6] or "CL" == data[6] or "EL" == data[6] or "BE1" == data[6] or "BESC" == data[6] or "RU1" == data[6] or "RUP" == data[6] or "UKR1" == data[6] or "UKRP" == data[6] or "TR1" == data[6]):
      newData.append(data)
  print(len(newData))
  return newData
  

def get_available_players(datas):
  appearances = get_appearances_required()
  #appearances = appearances[260000:]
  #playersAvalaible = []
  activePlayers = []
  
  for player in datas:
    if(player[16] != ""):
      activePlayers.append(player)
      
  with open('dataset/playerIds', 'w') as f:
    for player in activePlayers:
      available = [False, False, False, False]
      playerId = player[0]
      for app in appearances:
        if app[2] == playerId:
          if "2019" in app[4]:
            available[0] = True
          if "2020" in app[4]:
            available[1] = True
          if "2021" in app[4]:
            available[2] = True
          if "2022" in app[4]:
            available[3] = True
      if(available[0] == True and available[1] == True and available[2] == True and available[3] == True):
        #playersAvalaible.append(playerId)
        f.write(playerId)
        f.write(',')
  f.close()


def format_data():
  filePlayers = "dataset/players.csv"
  dataRawPlayers = open(filePlayers, "r").readlines()
  dataPlayers = []
  for line in dataRawPlayers :
    dataPlayers.append(line.split(','))
  dataPlayers = get_available_players(dataPlayers)
 
 
def get_players():
  filePlayers = "dataset/playerIds"
  dataRawPlayers = open(filePlayers, "r").readlines()
  dataPlayers = []
  for line in dataRawPlayers :
    dataPlayers = line.split(',')
  dataPlayers = dataPlayers[:len(dataPlayers)-1]
  return dataPlayers
  
  
def extract_league(appearances, id, startYear, endYear):
  appsPlayer = []
  for app in appearances:
    if(app[2] == id):
      appsPlayer.append(app)
  for apppl in appsPlayer:
    if(startYear in apppl[4] or endYear in apppl[4]):
      if(apppl[6] != "CL" and apppl[6] != "EL"):
        return apppl[6]
  if(len(appsPlayer) > 0):
    return appsPlayer[0][6]
  else:
    return 'NA'
   

def get_appearances_season(startYear, endYear):
  fileAppearances = "dataset/appearances.csv"
  dataRawAppearances = open(fileAppearances, "r").readlines()
  dataAppearances = []
  exploitableData = []
  
  for line in dataRawAppearances :
    dataAppearances.append(line.split(','))
  dataAppearances = dataAppearances[1:]
  
  for app in dataAppearances:
    if(startYear in app[4] or endYear in app[4]):
      exploitableData.append(app)
  appearances = []
  for data in exploitableData:
    if( "L1" == data[6] or "DFB" == data[6] or "DFL" == data[6] or "NL1" == data[6] or "NLP" == data[6] or "ES1" == data[6] or "CDR" == data[6] or "PO1" == data[6] or "POCP" == data[6] or "FR1" == data[6] or "GB1" == data[6] or "CGB" == data[6] or "IT1" == data[6] or "CIT" == data[6] or "CL" == data[6] or "EL" == data[6] or "BE1" == data[6] or "BESC" == data[6] or "RU1" == data[6] or "RUP" == data[6] or "UKR1" == data[6] or "UKRP" == data[6] or "TR1" == data[6]):
      appearances.append(data)
  print(len(appearances))
  return appearances   
   
  
def getChampionship():
  playerIds = get_players()
  appearances = get_appearances_season("2020", "2021")
  with open('dataset/playerLeagues', 'w') as f:
    for id in playerIds:
      f.write(extract_league(appearances, id, "2020-12", "2021-01"))
      f.write(',')
  f.close()
  appearancesLastSeason = get_appearances_season("2019", "2020")
  with open('dataset/playerPreviousLeagues', 'w') as file:
    for id in playerIds:
      file.write(extract_league(appearancesLastSeason, id, "2019-12", "2020-01"))
      file.write(',')
  file.close()


def get_ages():
  playerIds = get_players()
  filePlayers = "dataset/players.csv"
  dataRawPlayers = open(filePlayers, "r").readlines()
  dataPlayers = []
  for line in dataRawPlayers :
    dataPlayers.append(line.split(','))
  with open('dataset/playersAge', 'w') as file:
    for id in playerIds:
      for pl in dataPlayers:
        if(id == pl[0]):
          file.write(str(2021-int(pl[7].split('-')[0])))
          file.write(',')
  file.close()
  print("end")
    

def get_values():
  playerIds = get_players()
  filePrices = "dataset/player_valuations.csv"
  dataRawPrices = open(filePrices, "r").readlines()
  dataPrices = []
  for line in dataRawPrices :
    dataPrices.append(line.split(','))
  
  with open('dataset/playersPrices', 'w') as file:
    for id in playerIds:
      pricesId = []
      for price in dataPrices:
        if(id == price[3] and '2020' in price[0]):
          pricesId.append(price)
      file.write(pricesId[0][5])
      file.write(",")
  file.close()


def get_exact_season_appearance():
  allAppearances = get_appearances_season("2020", "2021")
  exactAppearances = []
  for app in allAppearances:
    if("2020-08" in app[4] or "2020-09" in app[4] or "2020-10" in app[4] or "2020-11" in app[4] or "2020-12" in app[4] or "2021-01" in app[4] or "2021-02" in app[4] or "2021-03" in app[4] or "2021-04" in app[4] or "2021-05" in app[4] or "2021-06" in app[4]):
      exactAppearances.append(app)
  playerIds = get_players()
  with open('dataset/minutesPlayed', 'w') as file:
    for id in playerIds:
      totalMinutes = 0
      for app in exactAppearances:
        if(id == app[2]):
          totalMinutes = totalMinutes + int(app[11])
      file.write(str(totalMinutes))
      file.write(',')
  file.close()
  
  
def get_exact_last_season_appearance():
  allAppearances = get_appearances_season("2019", "2020")
  exactAppearances = []
  for app in allAppearances:
    if("2019-08" in app[4] or "2019-09" in app[4] or "2019-10" in app[4] or "2019-11" in app[4] or "2019-12" in app[4] or "2020-01" in app[4] or "2020-02" in app[4] or "2020-03" in app[4] or "2020-04" in app[4] or "2020-05" in app[4] or "2020-06" in app[4]):
      exactAppearances.append(app)
  playerIds = get_players()
  with open('dataset/minutesPlayedPrevious', 'w') as file:
    for id in playerIds:
      totalMinutes = 0
      for app in exactAppearances:
        if(id == app[2]):
          totalMinutes = totalMinutes + int(app[11])
      file.write(str(totalMinutes))
      file.write(',')
  file.close()
       
 
def get_positions():
  playerIds = get_players()
  filePlayers = "dataset/players.csv"
  dataRawPlayers = open(filePlayers, "r").readlines()
  dataPlayers = []
  for line in dataRawPlayers :
    dataPlayers.append(line.split(','))    
  
  with open('dataset/positions', 'w') as file:
    for id in playerIds:
      for data in dataPlayers:
        if(id == data[0]):
          position = data[8]
          file.write(position)
          file.write(',')
  file.close()
 
  
def get_conceded_goal(appearance, dataGames):
  gameId = appearance[1]
  teamId = appearance[3]
  goalConceded = 0
  
  for game in dataGames:
    if(game[0] == gameId):
      if(game[6] == teamId):
        goalConceded = game[9]
      else:
        goalConceded = game[8]
  return goalConceded
  
       
def get_performance(startYear, endYear):
  allAppearances = get_appearances_season(startYear, endYear)
  exactAppearances = []
  for app in allAppearances:
    if(startYear+"-08" in app[4] or startYear+"-09" in app[4] or startYear+"-10" in app[4] or startYear+"-11" in app[4] or startYear+"-12" in app[4] or endYear+"-01" in app[4] or endYear+"-02" in app[4] or endYear+"-03" in app[4] or endYear+"-04" in app[4] or endYear+"-05" in app[4] or endYear+"-06" in app[4]):
      exactAppearances.append(app)
  playerIds = get_players()
  
  filePositions = "dataset/positions"
  positions = open(filePositions, "r").readlines()[0].split(',')
  
  fileGames = "dataset/games.csv"
  dataGames = open(fileGames, 'r').readlines()
  newDataGames = []
  for game in dataGames:
    newDataGames.append(game.split(','))
  newDataGames = newDataGames[1:]
  i = 0
  with open('dataset/performances', 'w') as file:
    for id in playerIds:
      perfPlayer = 0.0
      for app in exactAppearances:
        if(id == app[2]):
          if(positions[i] == "Defender" or positions[i] == "Goalkeeper"):
            perfPlayer = perfPlayer - float(get_conceded_goal(app, newDataGames))
          if(positions[i] == "Attack"):
            perfPlayer = perfPlayer + 0.8*float(app[9]) + 0.2*float(app[10])
          if(positions[i] == "Midfield"):
            perfPlayer = perfPlayer + 0.2*float(app[9]) + 0.8*float(app[10])
      if(perfPlayer < 0.0):
        perfPlayer = 1 / abs(perfPlayer)  
      else:
        perfPlayer = 1 / (60-perfPlayer) 
      file.write(str(perfPlayer))  
      file.write(',')    
      i=i+1
  file.close()
  
  
def set_perf_ratio():
  filePerf = "dataset/performancesPrevious"
  performances = open(filePerf, "r").readlines()[0].split(',')
  fileMinutes = "dataset/minutesPlayedPrevious"
  minutes = open(fileMinutes, "r").readlines()[0].split(',')
  with open('dataset/performanceRatiosPrevious', 'w') as file:
    i = 0
    for perf in performances:
      if(float(minutes[i]) != 0.0):
        ratio = float(perf) / (float(minutes[i])/90.0)
      else:
        ratio = 0.0
      file.write(str(ratio))
      file.write(',')
      i=i+1
  file.close()
  

def set_perf_variation():
  filePerf = "dataset/performanceRatios"
  perfs = open(filePerf, "r").readlines()[0].split(',')
  filePerfPrevious = "dataset/performanceRatiosPrevious"
  perfsPrevious = open(filePerfPrevious, "r").readlines()[0].split(',')
  with open('dataset/performanceVariation', 'w') as file:
    i = 0
    for perf in perfs:
      if(float(perf) - float(perfsPrevious[i]) < 0):
        file.write(str(0))
      else:
        file.write(str(1))
      file.write(',')
      i = i+1
  file.close()
  
  
def set_minutes_variation():
  fileMinutes = "dataset/minutesPlayed"
  minutes = open(fileMinutes, "r").readlines()[0].split(',')
  fileMinutesPrevious = "dataset/minutesPlayedPrevious"
  minutesPrevious = open(fileMinutesPrevious, "r").readlines()[0].split(',')
  with open('dataset/minutesVariation', 'w') as file:
    i = 0
    for minute in minutes:
      file.write(str(float(minute) - float(minutesPrevious[i])))
      file.write(',')
      i = i+1
  file.close()


def set_league_variation():
  fileLeague = "dataset/playerLeagues"
  leagues = open(fileLeague, "r").readlines()[0].split(',')
  fileLeaguePrevious = "dataset/playerPreviousLeagues"
  leaguePrevious = open(fileLeaguePrevious, "r").readlines()[0].split(',')
  with open('dataset/leagueVariation', 'w') as file:
    i=0
    for league in leagues:
      file.write(str( float(leaguesLabel[league]) - float(leaguesLabel[leaguePrevious[i]])))
      file.write(',')
      i=i+1
  file.close()
  
  
def write_data_input():
  performances = open('dataset/performanceRatios', "r").readlines()[0].split(',')
  vPerformance = open('dataset/performanceVariation', "r").readlines()[0].split(',')
  minutesPlayed = open('dataset/minutesPlayed', "r").readlines()[0].split(',')
  vMinutesPlayed = open('dataset/minutesVariation', "r").readlines()[0].split(',')
  ages = open('dataset/playersAge', "r").readlines()[0].split(',')
  leagues = open('dataset/playerLeagues', "r").readlines()[0].split(',')
  vLeagues = open('dataset/leagueVariation', "r").readlines()[0].split(',')
  prices = open('dataset/playersPrices', "r").readlines()[0].split(',')
  with open('dataset/inputData', 'w') as file:
    i = 0
    for age in ages:
      file.write(str(performances[i])+",")
      file.write(str(vPerformance[i])+",")
      file.write(str(float(minutesPlayed[i])/90.0)+",")
      file.write(str(float(vMinutesPlayed[i])/90.0)+",")
      file.write(str(age)+",")
      if int(age)<32:
        file.write(str(1)+",")
      else:
        file.write(str(0)+",")
      file.write(str(leaguesLabel[leagues[i]])+",")
      file.write(str(vLeagues[i])+",")
      file.write(str(float(prices[i]) / 100000.0))
      file.write("\n")
      i = i + 1
  file.close()
  

def get_old_price(idPlayer):
  filePrices = "dataset/player_valuations.csv"
  dataRawPrices = open(filePrices, "r").readlines()
  dataPrices = []
  for line in dataRawPrices :
    dataPrices.append(line.split(','))
  pricesId = []
  for price in dataPrices:
    if(idPlayer == price[3] and '2020' in price[0]):
      pricesId.append(price)
  return float(pricesId[len(pricesId) - 1][5])
  
  

def write_output_data():
  playerIds = get_players()
  filePrices = "dataset/player_valuations.csv"
  dataRawPrices = open(filePrices, "r").readlines()
  dataPrices = []
  for line in dataRawPrices :
    dataPrices.append(line.split(','))
  
  with open('dataset/outputData', 'w') as file:
    allPrices = []
    for id in playerIds:
      pricesId = []
      for price in dataPrices:
        if(id == price[3] and '2021' in price[0]):
          pricesId.append(price)
        #print('prices id ', pricesId)
      if(len(pricesId) > 0):
        #allPrices.append(float(pricesId[len(pricesId) - 1][5]))
        allPrices.append(float(pricesId[0][5])/100000.0)
      else:
        allPrices.append(get_old_price(id) / 100000.0)
    file.write(str(allPrices))
  file.close()  



#format_data()
#get_appearances_required()
#getChampionship()
#get_players()
#get_ages()
#get_values()
#get_exact_last_season_appearance()
#get_positions()
#get_performance()
#get_performance("2020", "2021")
#set_perf_ratio()
#set_perf_variation()
#set_minutes_variation()
#set_league_variation()
#write_data_input()
#write_output_data()
