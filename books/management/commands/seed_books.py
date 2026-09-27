from django.core.management.base import BaseCommand
from books.models import Book

BOOKS = [
    ("The Hobbit","J.R.R. Tolkien","Fantasy",1937,4.7,310,"A reluctant homebody joins dwarves on a quest to reclaim treasure from a dragon.","Bilbo Baggins is swept into an adventure involving dwarves, dragons and a dangerous journey.","Bilbo Baggins, Gandalf, Thorin Oakenshield","quest, courage, home"),
    ("Dune","Frank Herbert","Science Fiction",1965,4.7,412,"A young heir navigates politics and prophecy on a harsh desert planet.","Paul Atreides is drawn into a struggle involving politics, prophecy and the desert world of Arrakis.","Paul Atreides, Lady Jessica, Duke Leto","power, ecology, destiny"),
    ("Pride and Prejudice","Jane Austen","Romance",1813,4.7,432,"Wit and pride collide as Elizabeth Bennet navigates love and class.","Elizabeth Bennet and Mr. Darcy overcome pride and prejudice while navigating society and relationships.","Elizabeth Bennet, Mr. Darcy","love, class, wit"),
    ("The Silent Patient","Alex Michaelides","Mystery",2019,4.5,325,"A therapist becomes obsessed with treating a woman who has not spoken since a murder.","Alicia Berenson stops speaking after being accused of killing her husband, leading to a psychological mystery.","Alicia Berenson, Theo Faber","obsession, trauma, secrets"),
    ("Gone Girl","Gillian Flynn","Thriller",2012,4.3,432,"A woman's disappearance turns her husband into the prime suspect.","Nick Dunne becomes the prime suspect after Amy disappears, revealing secrets in their marriage.","Nick Dunne, Amy Dunne","marriage, deception, media"),
    ("Atomic Habits","James Clear","Self-Help",2018,4.8,320,"A practical guide to building good habits through small changes.","The book explains systems and small improvements that can make habits easier to build and maintain.","","habits, discipline, self-improvement"),
    ("Steve Jobs","Walter Isaacson","Biography",2011,4.6,656,"A detailed biography of Apple's co-founder.","The biography follows Jobs from childhood through his career at Apple and other companies.","Steve Jobs, Steve Wozniak","innovation, ambition, legacy"),
    ("Rich Dad Poor Dad","Robert Kiyosaki","Business & Finance",1997,4.3,336,"A personal finance book about money, assets and financial thinking.","The book contrasts two approaches to money and emphasizes financial literacy.","","money, assets, financial literacy"),
    ("The Pragmatic Programmer","Andrew Hunt & David Thomas","Technology & AI",1999,4.5,352,"A practical guide to writing better software.","A collection of principles and habits for software developers and engineers.","","programming, coding, software"),
    ("Sapiens","Yuval Noah Harari","History & Politics",2011,4.6,443,"A broad history of how Homo sapiens came to dominate the planet.","The book explores human history, cooperation, culture and civilization.","","history, civilization, anthropology"),
    ("Cosmos","Carl Sagan","Science & Math",1980,4.7,365,"An accessible tour of the universe and scientific discovery.","Sagan explores the universe, life, science and humanity's place within the cosmos.","","astronomy, science, discovery"),
    ("Life of Pi","Yann Martel","Adventure",2001,4.4,319,"A shipwrecked boy shares a lifeboat with a Bengal tiger.","Pi Patel survives at sea with Richard Parker in a story of survival, faith and storytelling.","Pi Patel, Richard Parker","survival, faith, storytelling"),
    ("1984","George Orwell","Dystopian",1949,4.6,328,"A man begins to question an all-seeing authoritarian society.","Winston Smith struggles against surveillance and control under the Party.","Winston Smith, Julia","surveillance, control, truth"),
    ("The Shining","Stephen King","Horror",1977,4.5,447,"A family's stay at an isolated hotel becomes terrifying.","Jack Torrance and his family face the dark history of the Overlook Hotel.","Jack Torrance, Danny Torrance","isolation, family, fear"),
    ("Meditations","Marcus Aurelius","Philosophy",180,4.6,254,"Stoic reflections on duty, mortality and self-control.","Private reflections on Stoic principles and living with discipline and equanimity.","","stoicism, duty, mortality"),
]

class Command(BaseCommand):
    help = "Add sample books to the database"

    def handle(self, *args, **kwargs):
        for data in BOOKS:
            Book.objects.update_or_create(title=data[0], defaults={
                "author": data[1], "genre": data[2], "year": data[3],
                "rating": data[4], "pages": data[5], "description": data[6],
                "summary": data[7], "characters": data[8], "themes": data[9]
            })
        self.stdout.write(self.style.SUCCESS("Sample books added successfully."))
