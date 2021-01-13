import requests

from enum import Enum
from typing import List

class PlayerMatchMode(Enum):
    ARENA = 'arena'
    CAMPAIGN = 'campaign'
    CUSTOM = 'custom'
    WARZONE = 'warzone'

class WaypointHalo5:
    subscription_key: str
    api_session = None

    def __init__(self, subscription_key: str):
        self.subscription_key = subscription_key
        api_session = requests.Session()
        api_session.headers.update({ 'Ocp-Apim-Subscription-Key': subscription_key })
        self.api_session = api_session

    def get_player_match_history(self, player_id: str, modes: List[PlayerMatchMode] = [], start: int = 0, count: int = 25, include_times=False) -> dict:
        str_modes = list(map(lambda x: str(x.value), modes))
        seralized_modes = ", ".join(str_modes)
        print('seralized_modes', seralized_modes)

        response = self.api_session.get(
            f'https://www.haloapi.com/stats/h5/players/{player_id}/matches?'
            f'modes={seralized_modes}&start={start}&count={count}&include-times={str(include_times).lower()}'
        )

        return response.json()

    def get_match_result_warzone(self, match_id: str):
        response = self.api_session.get(f'https://www.haloapi.com/stats/h5/warzone/matches/{match_id}')
        return response.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--k', '--apikey', help="api key for halo 5 waypoint", type=str)
    
    args = parser.parse_args()

    wp = WaypointHalo5(args.apiKey)
    response = wp.get_player_match_history(player_id='CobolOnCloud', modes=[PlayerMatchMode.WARZONE], count=5)
    api_keys = list(map(lambda x: x["Id"]["MatchId"], response["Results"])))

    assert len(api_keys) == 5
