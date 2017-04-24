#les objets de base
from soccersimulator import Vector2D, SoccerState, SoccerAction

#objets pour un match
from soccersimulator import Simulation, SoccerTeam, Player, show_simu, SoccerTournament

#importer la strategie de base
from soccersimulator import Strategy

#toutes les constantes
from soccersimulator import settings

#module math
import math

from golf import Golf, Slalom


team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("Golf",Golf())
team2.add("Slalom", Slalom())
def get_golf_team():
	return team1

def get_slalom_team1():
	return team2

