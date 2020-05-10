from django.core.management import BaseCommand
from django.db.models.functions import datetime

from apps.league.models import LeagueUser, Competition, Category, Team, Ranking, Submit, Files


class Command(BaseCommand):
    CATEGORY_NAMES = ['Cryptography', 'AI', 'Blockchain', 'Machine Learning', 'Deep Learning',
                      'Reinforcement Learning', 'Complexity']
    CATEGORY_DESC = [
        'Cryptography or cryptology is the practice and study of techniques for secure communication in the presence '
        'of third parties called adversaries.',
        'Artificial Intelligence is intelligence demonstrated by machines, in contrast to the natural intelligence '
        'displayed by humans and animals.',
        'Blockchain is a growing list of records, called blocks, that are linked using cryptography. Each block '
        'contains a cryptographic hash of the previous block, a timestamp, and transaction data.',
        'ML  is the study of computer algorithms that improve automatically through experience. It is seen as a '
        'subset of artificial intelligence.Machine learning algorithms build a mathematical model based on sample '
        'data, known as "training data", in order to make predictions or decisions without being explicitly '
        'programmed to do so.',
        'Deep Learning is part of a broader family of machine learning methods based on artificial neural networks '
        'with representation learning. Learning can be supervised, semi-supervised or unsupervised.',
        'Reinforcement Learning is an area of machine learning concerned with how software agents ought to take '
        'actions in an environment in order to maximize the notion of cumulative reward. Reinforcement learning is '
        'one of three basic machine learning paradigms, alongside supervised learning and unsupervised learning.',
        'Are you good enough to develop the best efficient programs? You should try one of this competitions!',
    ]

    USERS_NAME = ['latra', 'Oriolac', 'Marta99', 'sergisi', 'quimpm', 'horno', 'Doasy', 'pau1838', 'notaiax']
    GITHUB = 'https://github.com/'
    USERS = {}

    def handle(self, *args, **options):
        admin = LeagueUser.objects.create_superuser(username='admin', password='admin')
        admin.save()
        for name in self.USERS_NAME:
            user = LeagueUser.objects.create(username=name, email=f'{name}@gmail.com',
                                             github_link=f'{self.GITHUB}{name}')
            user.set_password(r'password')
            self.USERS[user.username] = user
            user.save()

        cats = []
        for name, desc in zip(self.CATEGORY_NAMES, self.CATEGORY_DESC):
            cat = Category.objects.create(name=name, description=desc)
            cats.append(cat)
            cat.save()
        comp = Competition.objects.create(title='I Blockchain League',
                                          description='Now it comes the I Blockchain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2012, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2013, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2015, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2017, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()

        team = Team.objects.create(name='Patatas de Gimeno')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['Marta99'])
        team.competition = comp
        team.ranking = Ranking.create(100).save()
        team.submition = Submit.objects.create(description='Submition of Patatas de Gimeno',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2016, month=5, day=10, hour=20,
                                                                             minute=23, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()


        team = Team.objects.create(name='CodePlayers')
        team.members.add(self.USERS['pau1838'])
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['sergisi'])
        team.members.add(self.USERS['Doasy'])
        team.competition = comp
        team.ranking = Ranking.create(95).save()
        team.submition = Submit.objects.create(description='Submition of CodePlayers',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2016, month=6, day=5, hour=10,
                                                                             minute=45, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()


        comp = Competition.objects.create(title='II Blockchain League',
                                          description='Now it comes the II Blockchain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2018, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2022, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()

        team = Team.objects.create(name='SegmentationFault')
        team.members.add(self.USERS['notaiax'])
        team.members.add(self.USERS['pau1838'])
        team.members.add(self.USERS['horno'])
        team.competition = comp
        team.ranking = Ranking.create(80).save()
        team.submition = Submit.objects.create(description='Submition of SegmentationFault',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=6, day=5, hour=22,
                                                                             minute=45, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='LeetCode')
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['Oriolac'])
        team.competition = comp
        team.ranking = Ranking.create(70).save()
        team.submition = Submit.objects.create(description='Submition of LeetCode',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2021, month=3, day=20, hour=17,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Team League')
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['sergisi'])
        team.competition = comp
        team.ranking = Ranking.create(70).save()
        team.submition = Submit.objects.create(description='Submition of LeetCode',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2021, month=3, day=20, hour=17,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='III Blockchain League',
                                          description='Now it comes the III Blockchain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2021, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2021, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()

        team = Team.objects.create(name='APIs4Win')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['pau1838'])
        team.competition = comp
        team.ranking = Ranking.create(90).save()
        team.submition = Submit.objects.create(description='Submition of APIs4Win',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2021, month=7, day=20, hour=17,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Haskellerians')
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['sergisi'])
        team.competition = comp
        team.ranking = Ranking.create(105).save()
        team.submition = Submit.objects.create(description='Submition of Haskellerians',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=3, day=7, hour=19,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='SuperCoders')
        team.members.add(self.USERS['Doasy'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(55).save()
        team.submition = Submit.objects.create(description='Submition of Supercoders',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=5, day=13, hour=19,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='I Deep Learning League',
                                          description='LleidaHack has creted the first Deep Learning League. You can '
                                                      'join the league before competition starts.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[1])
        comp.categories.add(cats[3])
        comp.categories.add(cats[4])
        comp.categories.add(cats[5])
        comp.save()

        team = Team.objects.create(name='Lethal')
        team.members.add(self.USERS['Doasy'])
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Marta99'])
        team.competition = comp
        team.ranking = Ranking.create(120).save()
        team.submition = Submit.objects.create(description='Submition of Lethal',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2023, month=10, day=7, hour=19,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='PHPHaters')
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(140).save()
        team.submition = Submit.objects.create(description='Submition of PHPHaters',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2023, month=5, day=20, hour=22,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='II Deep Learning League',
                                          description='LleidaHack has creted the second Deep Learning League. You can '
                                                      'join the league before competition starts.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2018, month=4, day=10, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=5, day=11, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2020, month=5, day=15, hour=20,
                                                                                   minute=30, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2025, month=5, day=31, hour=20,
                                                                                    minute=30, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[1])
        comp.categories.add(cats[3])
        comp.categories.add(cats[4])
        comp.categories.add(cats[5])
        comp.save()

        team = Team.objects.create(name='Aniquilators')
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['sergisi'])
        team.competition = comp
        team.ranking = Ranking.create(130).save()
        team.submition = Submit.objects.create(description='Submition of Aniquilators',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=5, day=17, hour=22,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Dominators')
        team.members.add(self.USERS['Doasy'])
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['pau1838'])
        team.competition = comp
        team.ranking = Ranking.create(170).save()
        team.submition = Submit.objects.create(description='Submition of Dominators',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=5, day=20, hour=23,
                                                                             minute=45, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='I Data Jam',
                                          description='Data Jam is a competition where the teams have to develop '
                                                      'programs to solve some high-complex problems. Are you '
                                                      'prepared?',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2016, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2018, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2018, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2029, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()

        team = Team.objects.create(name='Code Warriors')
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['pau1838'])
        team.members.add(self.USERS['Oriolac'])
        team.competition = comp
        team.ranking = Ranking.create(90).save()
        team.submition = Submit.objects.create(description='Submition of Code Warriors',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2023, month=7, day=1, hour=12,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='The Bytes')
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(110).save()
        team.submition = Submit.objects.create(description='Submition of The Bytes',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2023, month=5, day=20, hour=22,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Veterans')
        team.members.add(self.USERS['Doasy'])
        team.members.add(self.USERS['sergisi'])
        team.competition = comp
        team.ranking = Ranking.create(100).save()
        team.submition = Submit.objects.create(description='Submition of Veterans',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2025, month=6, day=12, hour=22,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='II Data Jam',
                                          description='Data Jam is a competition where the teams have to develop '
                                                      'programs to solve some high-complex problems. Are you '
                                                      'prepared?',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()

        team = Team.objects.create(name='Your Worst Nightmare')
        team.members.add(self.USERS['sergisi'])
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['pau1838'])
        team.competition = comp
        team.ranking = Ranking.create(90).save()
        team.submition = Submit.objects.create(description='Submition of Your Worst Nightmare',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=5, day=25, hour=15,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Challengers')
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(85).save()
        team.submition = Submit.objects.create(description='Submition of Challengers',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=4, day=9, hour=17,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='III Data Jam',
                                          description='Data Jam is a competition where the teams have to develop '
                                                      'programs to solve some high-complex problems. Are you '
                                                      'prepared? Here it comes the 3rd edition!',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()

        team = Team.objects.create(name='Unbeatables')
        team.members.add(self.USERS['sergisi'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['Doasy'])
        team.competition = comp
        team.ranking = Ranking.create(85).save()
        team.submition = Submit.objects.create(description='Submition of Unbeatables',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2024, month=2, day=9, hour=21,
                                                                             minute=35, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='I Cybersecurity League',
                                          description='For lovers of computer security, here it comes the first '
                                                      'edition of the Cybersecurity League',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2019, month=8, day=20, hour=11,
                                                                                   minute=30, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2022, month=9, day=20, hour=11,
                                                                                    minute=15, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2022, month=8, day=21, hour=20,
                                                                                   minute=00, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2030, month=8, day=25, hour=20,
                                                                                    minute=00, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.save()

        team = Team.objects.create(name='Cyberfighters')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['notaiax'])
        team.members.add(self.USERS['horno'])
        team.competition = comp
        team.ranking = Ranking.create(95).save()
        team.submition = Submit.objects.create(description='Submition of Cyberfighters',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=8, day=22, hour=17,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Cyber Kings')
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['Oriolac'])
        team.competition = comp
        team.ranking = Ranking.create(70).save()
        team.submition = Submit.objects.create(description='Submition of Cyber Kings',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=8, day=24, hour=19,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='II Cybersecurity League',
                                          description='For lovers of computer security, and as the first edition was '
                                                      'so successful. Here it comes the second edition of the '
                                                      'Cybersecurity League',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.save()

        team = Team.objects.create(name='Tech Divas')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Doasy'])
        team.members.add(self.USERS['Marta99'])
        team.competition = comp
        team.ranking = Ranking.create(100).save()
        team.submition = Submit.objects.create(description='Submition of Tech Divas',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=8, day=25, hour=12,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Cyberlovers')
        team.members.add(self.USERS['pau1838'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(85).save()
        team.submition = Submit.objects.create(description='Submition of Cyberlovers',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2023, month=5, day=14, hour=11,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Workaholics')
        team.members.add(self.USERS['sergisi'])
        team.members.add(self.USERS['Oriolac'])
        team.competition = comp
        team.ranking = Ranking.create(100).save()
        team.submition = Submit.objects.create(description='Submition of Workaholics',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2020, month=11, day=29, hour=23,
                                                                             minute=00, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='Code Squad')
        team.members.add(self.USERS['quimpm'])
        team.members.add(self.USERS['horno'])
        team.competition = comp
        team.ranking = Ranking.create(85).save()
        team.submition = Submit.objects.create(description='Submition of CodeSquad',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2022, month=6, day=22, hour=20,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='I SATSolver Race',
                                          description='For the first time, here it comes the first SATSolver Race! '
                                                      'Will you be the fastest solver?',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()

        team = Team.objects.create(name='estresSAT')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['Doasy'])
        team.competition = comp
        team.ranking = Ranking.create(100).save()
        team.submition = Submit.objects.create(description='Submition of estreSAT Solver',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2019, month=9, day=10, hour=20,
                                                                             minute=23, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='fracaSAT')
        team.members.add(self.USERS['sergisi'])
        team.members.add(self.USERS['horno'])
        team.members.add(self.USERS['notaiax'])
        team.competition = comp
        team.ranking = Ranking.create(80).save()
        team.submition = Submit.objects.create(description='Submition of fracaSAT Solver',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2021, month=5, day=10, hour=15,
                                                                             minute=23, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        team = Team.objects.create(name='The Best SAT')
        team.members.add(self.USERS['pau1838'])
        team.members.add(self.USERS['quimpm'])
        team.competition = comp
        team.ranking = Ranking.create(75).save()
        team.submition = Submit.objects.create(description='Submition of The Best SAT Solver',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2021, month=4, day=22, hour=20,
                                                                             minute=30, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()
