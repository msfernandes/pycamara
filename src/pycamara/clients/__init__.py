from pycamara.clients.blocks import BlockClient
from pycamara.clients.congressmen import CongressmanClient
from pycamara.clients.events import EventClient
from pycamara.clients.legislative_bodies import LegislativeBodyClient
from pycamara.clients.legislatures import LegislatureClient
from pycamara.clients.parties import PartyClient
from pycamara.clients.propositions import PropositionClient
from pycamara.clients.references import ReferenceClient
from pycamara.clients.votings import VotingClient


class Client(object):
    pass


cd = Client()
cd.blocks = BlockClient()
cd.congressmen = CongressmanClient()
cd.events = EventClient()
cd.legislative_bodies = LegislativeBodyClient()
cd.legislatures = LegislatureClient()
cd.parties = PartyClient()
cd.propositions = PropositionClient()
cd.references = ReferenceClient()
cd.votings = VotingClient()
