from datetime import datetime
from crewai import Task


class FootballNewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top football news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top Football news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {  'title': 'Germany will host the 2024 UEFA European Football Championship', 
                    'url': 'https://example.com/story1', 
                    'summary': 'Football made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. There should be at least 5 articles, each following the proper format.
                Example Output: 
                '## Germany will host the 2024 UEFA European Football Championship.\n\n
                **The Rundown:
                ** Euro 2024 will be the 17th edition of the UEFA European Championship...\n\n
                **The details:**\n\n
                - The tournament will take place from 14 June to 14 July 2024...\n\n
                **Why it matters:** It will be the third time that Europian Championship matches are played on Germany territory.\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                '# Top stories in football today:\\n\\n
                - Germany will host the 2024 UEFA European Football Championship.\\n
                - The 2024 Champions League final will be held in Wembley Stadium in London.\\n\\n

                ## Germany will host the 2024 UEFA European Football Championship.\\n\\n
                **The Rundown:** Euro 2024 will be the 17th edition of the UEFA European Championship...\\n\\n
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                ## Altman seeks TRILLIONS for global AI chip initiative\\n\\n
                **The Rundown:** It will be played between German club Borussia Dortmund and Spanish club Real Madrid...\\n\\n'
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
            """,
            callback=callback_function
        )