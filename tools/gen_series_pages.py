#!/usr/bin/env python3
"""Generate series/title pages that replace the old bookshop URLs, with Amazon.ie affiliate links.

    python3 tools/gen_series_pages.py && python3 tools/gen_redirects.py && python3 tools/build.py --check
"""
import os
import urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TAG = "childrensb09f-21"


def amz(q):
    return f"https://www.amazon.ie/s?k={urllib.parse.quote_plus(q)}&tag={TAG}"


def entry(title, meta, desc, q=None):
    btn = f'<p class="buybox"><a class="btn" href="{amz(q or title)}" rel="sponsored nofollow noopener" target="_blank">Check price on Amazon.ie</a></p>'
    return f"### {title}\n*{meta}*\n\n{desc}\n\n{btn}"


DISC = "*Affiliate disclosure: as an Amazon Associate we earn from qualifying purchases, at no extra cost to you. Prices and availability change, so check Amazon.ie.*"


def page(slug, title, h1, short, desc, image, alt, lede, related, intro, sections, faq, kind="guide", parent="guides", nav="/guides/"):
    fm = f"title: {title}\nh1: {h1}\nshort: {short}\ndescription: {desc}\nkind: {kind}\nnav: {nav}\nparent: {parent}\nimage: {image}\nalt: {alt}\nlede: {lede}\nrelated: {related}\nupdated: 2026-11-16\n---\n"
    body = intro + "\n\n" + DISC + "\n\n" + "\n\n".join(sections) + "\n\n:::faq\n" + "\n\n".join(f"### {q}\n{a}" for q, a in faq) + "\n:::\n"
    open(os.path.join(ROOT, "content", slug + ".md"), "w", encoding="utf-8").write(fm + body)


def books(items):
    return ":::books\n" + "\n\n".join(entry(*i) for i in items) + "\n:::"


def main():
    # ---- Artemis Fowl
    af = [("Artemis Fowl", "Book 1, 2001", "A twelve-year-old criminal mastermind plans to steal fairy gold and discovers the fairy world is very real.", "Artemis Fowl Eoin Colfer"),
          ("Artemis Fowl: The Arctic Incident", "Book 2, 2002", "Artemis teams up with some unlikely allies in a rescue mission far from home.", "Artemis Fowl The Arctic Incident"),
          ("Artemis Fowl: The Eternity Code", "Book 3, 2003", "A dangerous invention falls into the wrong hands.", "Artemis Fowl The Eternity Code"),
          ("Artemis Fowl: The Opal Deception", "Book 4, 2005", "An old enemy returns with a plan for revenge.", "Artemis Fowl The Opal Deception"),
          ("Artemis Fowl: The Lost Colony", "Book 5, 2006", "A mystery leads to a hidden world.", "Artemis Fowl The Lost Colony"),
          ("Artemis Fowl: The Time Paradox", "Book 6, 2008", "Time travel enters the story.", "Artemis Fowl The Time Paradox"),
          ("Artemis Fowl: The Atlantis Complex", "Book 7, 2010", "Artemis is not himself in this later adventure.", "Artemis Fowl The Atlantis Complex"),
          ("Artemis Fowl: The Last Guardian", "Book 8, 2012", "The final book in the original series.", "Artemis Fowl The Last Guardian")]
    af = [(t, m, d, q) for t, m, d, q in af]
    page("artemis-fowl-books-in-order", "Artemis Fowl Books in Order | Complete Reading List", "Artemis Fowl books in order", "Artemis Fowl in order",
         "Artemis Fowl books in order: all eight Eoin Colfer novels plus the Fowl Twins spin-offs, with ages, reading tips and where to buy on Amazon.ie.",
         "series-artemis-fowl", "A night scene with glowing gems, gold coins, fairy wings and a lantern in a cave", "All eight Artemis Fowl novels in the right order, plus the Fowl Twins spin-offs.",
         "irish-childrens-authors,percy-jackson-books-in-order,alex-rider-books-in-order,books-for-early-readers",
         "**Artemis Fowl** is a fantasy adventure series by the Irish author Eoin Colfer. The first book was published in 2001 and follows a young criminal genius who sets out to steal fairy gold. Colfer, from Wexford, was Ireland’s Laureate na nÓg (children’s laureate) from 2014 to 2017. The books suit confident readers from about 9 or 10 and up.",
         ["## The eight Artemis Fowl books in order", books(af),
          "## The Fowl Twins spin-offs\n\nAfter the main series, Colfer wrote a spin-off trilogy about Artemis’s younger brothers: **The Fowl Twins** (2019), **The Fowl Twins: Deny All Charges** (2020) and **The Fowl Twins Get What They Deserve** (2021). They can be read after the main series.\n\n" + books([("The Fowl Twins", "Spin-off, 2019", "A new generation of Fowls.", "The Fowl Twins Eoin Colfer")]),
          "## Which age is Artemis Fowl for?\n\nMost children enjoy the series from about 9 to 12. The stories are fast and funny, with some peril and a lot of gadgets. Younger fans can listen to them read aloud.",
          "## If you like Artemis Fowl\n\nTry the [Percy Jackson books in order](/percy-jackson-books-in-order/) or the [Alex Rider books in order](/alex-rider-books-in-order/). Looking for more Irish writers? See [Irish children’s authors](/irish-childrens-authors/)."],
         [("What order should I read the Artemis Fowl books in?", "Read them in publication order, starting with Artemis Fowl and ending with The Last Guardian. The Fowl Twins books come after."),
          ("How many Artemis Fowl books are there?", "Eight in the main series, plus three Fowl Twins spin-off books."),
          ("Is Eoin Colfer Irish?", "Yes. He is from Wexford and was Laureate na nÓg from 2014 to 2017."),
          ("What age is Artemis Fowl for?", "About 9 to 12, although many older readers enjoy it too.")])
    # ---- Percy Jackson
    pj = [("The Lightning Thief", "Book 1, 2005", "Percy discovers he is the son of a Greek god and is sent to Camp Half-Blood.", "Percy Jackson and the Lightning Thief Rick Riordan"),
          ("The Sea of Monsters", "Book 2, 2006", "Percy and his friends set out on a quest across dangerous waters.", "Percy Jackson and the Sea of Monsters"),
          ("The Titan’s Curse", "Book 3, 2007", "A rescue mission takes Percy and his friends into peril.", "Percy Jackson and the Titan's Curse"),
          ("The Battle of the Labyrinth", "Book 4, 2008", "A maze of tunnels holds new dangers.", "Percy Jackson and the Battle of the Labyrinth"),
          ("The Last Olympian", "Book 5, 2009", "The series reaches its final battle.", "Percy Jackson and the Last Olympian")]
    page("percy-jackson-books-in-order", "Percy Jackson Books in Order | Reading Guide", "Percy Jackson books in order", "Percy Jackson in order",
         "Percy Jackson books in order: the five Olympians novels, then Heroes of Olympus and more by Rick Riordan, with ages and where to buy on Amazon.ie.",
         "series-percy-jackson", "Greek-style columns beside a blue sea with a trident under a sunny sky", "The five Percy Jackson and the Olympians books in order, and where to go next.",
         "rick-riordan,camp-half-blood-the-wild-zone,artemis-fowl-books-in-order,the-hobbit",
         "**Percy Jackson and the Olympians** is a series of five fantasy novels by [Rick Riordan](/rick-riordan/), starting with *The Lightning Thief*, published in 2005. They follow a boy who learns that the Greek gods are real and that he is the son of one of them. They suit readers aged about 9 to 13.",
         ["## The five Percy Jackson books in order", books(pj),
          "## What to read after the five books\n\nRiordan’s later series share the same world: **The Heroes of Olympus**, **The Trials of Apollo**, and others. A newer story in the Percy Jackson world, [Camp Half-Blood: The Wild Zone](/camp-half-blood-the-wild-zone/), is in our current Top 20 children’s books.",
          "## Which age is Percy Jackson for?\n\nAbout 9 to 13. The stories are fast-moving and funny, with action and some scary moments. They make a good read-aloud for younger children if you are happy to skip the scariest bits.",
          "## If you like Percy Jackson\n\nTry [Artemis Fowl](/artemis-fowl-books-in-order/), [The Hobbit](/the-hobbit/) and [Harry Potter](/harry-potter-and-the-philosophers-stone/)."],
         [("What order should I read Percy Jackson in?", "Start with The Lightning Thief and read the five Olympians books in order. Then move on to The Heroes of Olympus."),
          ("How many Percy Jackson books are there?", "Five in the original Percy Jackson and the Olympians series, with several follow-up series in the same world."),
          ("What age is Percy Jackson for?", "About 9 to 13."),
          ("Who wrote Percy Jackson?", "Rick Riordan, an American author who taught middle school before writing full-time.")])
    # ---- Alex Rider
    ar = [("Stormbreaker", "Book 1, 2000", "A fourteen-year-old is recruited as a spy after his uncle’s death.", "Stormbreaker Anthony Horowitz"),
          ("Point Blanc", "Book 2, 2001", "A mission takes Alex to a school with a secret.", "Point Blanc Anthony Horowitz"),
          ("Skeleton Key", "Book 3, 2002", "Alex is sent to a dangerous location.", "Skeleton Key Anthony Horowitz"),
          ("Eagle Strike", "Book 4, 2003", "A new threat appears.", "Eagle Strike Anthony Horowitz"),
          ("Scorpia", "Book 5, 2004", "Alex faces a criminal organisation.", "Scorpia Anthony Horowitz"),
          ("Ark Angel", "Book 6, 2005", "A high-risk mission with global stakes.", "Ark Angel Anthony Horowitz"),
          ("Snakehead", "Book 7, 2007", "A new case takes Alex to Asia.", "Snakehead Anthony Horowitz"),
          ("Crocodile Tears", "Book 8, 2009", "Alex investigates a charity with a secret.", "Crocodile Tears Anthony Horowitz"),
          ("Scorpia Rising", "Book 9, 2011", "A final confrontation approaches.", "Scorpia Rising Anthony Horowitz")]
    page("alex-rider-books-in-order", "Alex Rider Books in Order | Complete Reading List", "Alex Rider books in order", "Alex Rider in order",
         "Alex Rider books in order, from Stormbreaker to Scorpia Rising, with the prequel Russian Roulette, suggested ages and where to buy on Amazon.ie.",
         "series-alex-rider", "A night city skyline with a searchlight beam and a spy’s briefcase", "Every Alex Rider spy novel in reading order, from Stormbreaker to Ark Angel and beyond.",
         "artemis-fowl-books-in-order,percy-jackson-books-in-order,books-for-early-readers,how-to-help-a-reluctant-reader",
         "**Alex Rider** is a spy thriller series by the British author Anthony Horowitz. The first book, *Stormbreaker*, was published in 2000 and follows a teenage boy recruited by British intelligence. Ark Angel is the sixth book. The series suits readers aged about 10 and up, as it contains peril and some violence.",
         ["## The Alex Rider books in order", books(ar),
          "## A prequel\n\n**Russian Roulette** (2013) is a prequel about the villain Yassen Gregorovich. It is best read after the main series.\n\n" + books([("Russian Roulette", "Prequel, 2013", "The backstory of a villain from the series.", "Russian Roulette Anthony Horowitz")]),
          "## Is Alex Rider suitable for my child?\n\nThe stories are thrilling and fast, with action and some darker moments. Most children enjoy them from about 10 or 11. Check the first book yourself if your child is younger.",
          "## If you like Alex Rider\n\nTry [Artemis Fowl](/artemis-fowl-books-in-order/) or [Percy Jackson](/percy-jackson-books-in-order/)."],
         [("What order should I read Alex Rider in?", "Publication order, starting with Stormbreaker. Read Russian Roulette last."),
          ("Where does Ark Angel come in the series?", "It is the sixth Alex Rider book, published in 2005, between Scorpia and Snakehead."),
          ("What age is Alex Rider for?", "About 10 and up."),
          ("Who wrote Alex Rider?", "Anthony Horowitz.")])
    # ---- Bluey
    bl = [("Bluey: Let’s Play Outside", "Picture book", "A Bluey story about outdoor play and imagination.", "Bluey Let's Play Outside"),
          ("Bluey: Where’s Bluey?", "Bluey book", "A Bluey book to look through together. Check the format on the product page.", "Bluey Where's Bluey"),
          ("Bluey: The Pool", "Board book", "A story with a splash, in a sturdy format for small hands.", "Bluey The Pool board book")]
    page("best-bluey-books-for-kids", "Best Bluey Books for Kids | Picture and Board Books", "Best Bluey books for kids", "Bluey books",
         "The best Bluey books for children aged 2 to 6: picture books, board books and search-and-find titles, with tips and links to buy on Amazon.ie.",
         "series-bluey", "A sunny backyard with a fence, a swing, a ball and flowers", "Books based on the hit animated series, for toddlers and preschoolers.",
         "books-for-preschoolers,bedtime-stories-for-children,best-peppa-pig-books,best-ladybird-books-for-children",
         "**Bluey** is an Australian animated series about a family of dogs that first aired in 2018. Its stories about family and imaginative play have inspired a large range of children’s books. Most Bluey books suit children aged about 2 to 6.",
         ["## Bluey books for children", books(bl),
          "## Choosing a Bluey book\n\n- **Board books** are sturdy and good for toddlers.\n- **Picture books** suit story time at bedtime.\n\nCheck the age range and format on the Amazon.ie page before you order.",
          "## Make reading a game\n\nBluey stories are all about play. Act out a scene, make up your own game or ask: what would you play outside today? See our [book activities for kids](/book-activities-for-kids-at-home/) for more ideas.",
          "## More for this age\n\nSee [books for preschoolers](/books-for-preschoolers/), [bedtime stories](/bedtime-stories-for-children/) and [the Peppa Pig books](/best-peppa-pig-books/)."],
         [("What age are Bluey books for?", "Usually about 2 to 6, depending on the format."),
          ("Are Bluey books good for toddlers?", "Yes. Board books are made for small hands and short attention spans."),
          ("What other books are like Bluey?", "Peppa Pig and The Gruffalo are popular with the same age group."),
          ("Where can I buy Bluey books?", "Use the links on this page to check price and availability on Amazon.ie.")])
    # ---- Peppa
    pp = [("Peppa Pig: Goodnight Peppa", "Bedtime story", "A calm story for the end of the day.", "Peppa Pig Goodnight Peppa"),
          ("Peppa Pig: I Love You, Mummy Pig", "Picture book", "A story about family love.", "Peppa Pig I Love You Mummy Pig"),
          ("Peppa Pig: Peppa and Friends", "Board book", "A board book about Peppa and her friends.", "Peppa Pig Peppa and Friends board book"),
          ("Peppa Pig: Peppa Goes to the Library", "Board book", "A story about visiting the library.", "Peppa Pig Peppa Goes to the Library board book"),
          ("Peppa Pig: Peppa Washing Day", "Board book", "An everyday story at home.", "Peppa Pig Peppa Washing Day board book")]
    page("best-peppa-pig-books", "Best Peppa Pig Books for Toddlers | Where to Buy", "Best Peppa Pig books for toddlers", "Peppa Pig books",
         "The best Peppa Pig books for toddlers and preschoolers: bedtime stories, board books and picture books, with ages and links to buy on Amazon.ie.",
         "series-peppa-pig", "Rainy puddles, red wellington boots and an umbrella under grey clouds", "Board books and bedtime stories for fans of the muddy-puddle-loving pig.",
         "books-for-preschoolers,bedtime-stories-for-children,best-bluey-books-for-kids,best-ladybird-books-for-children",
         "**Peppa Pig** is a British animated series, created by Neville Astley and Mark Baker, which began in 2004. The books follow Peppa, her little brother George and their family and friends through everyday adventures. They suit children aged about 1 to 5.",
         ["## Peppa Pig books", books(pp),
          "## Which Peppa book should I choose?\n\n- **Board books** are best for babies and toddlers.\n- **Picture books** suit bedtime and story time.\n- Pick a story that matches something your child is doing, such as visiting the library or washing day.",
          "## Make it a first library trip\n\nAfter reading Peppa Goes to the Library, visit your own library. See [children’s books and your local library](/childrens-books-and-your-local-library/).",
          "## More for this age\n\nSee [books for preschoolers](/books-for-preschoolers/), [bedtime stories](/bedtime-stories-for-children/) and [Bluey books](/best-bluey-books-for-kids/)."],
         [("What age are Peppa Pig books for?", "About 1 to 5, depending on the format."),
          ("Are Peppa Pig books good for bedtime?", "Goodnight Peppa and other calm stories work well at the end of the day."),
          ("Who created Peppa Pig?", "Neville Astley and Mark Baker."),
          ("Where can I buy Peppa Pig books?", "Use the links on this page to check price and availability on Amazon.ie.")])
    # ---- Ladybird
    lb = [("Ladybird Tales: The Enormous Turnip", "Hardback", "A traditional tale retold for young readers.", "Ladybird Tales The Enormous Turnip"),
          ("Ladybird Tales: The Magic Porridge Pot", "Hardback", "A folk tale about a pot that will not stop.", "Ladybird Tales The Magic Porridge Pot"),
          ("Ladybird Tales: Little Red Riding Hood", "Hardback", "A classic fairy tale for young readers.", "Ladybird Tales Little Red Riding Hood"),
          ("Ladybird Stories for 3 Year Olds", "Hardback collection", "A collection of short stories.", "Ladybird Stories for 3 Year Olds"),
          ("Ladybird First Favourite Nursery Rhymes", "Rhyme book", "Favourite rhymes in one book.", "Ladybird First Favourite Nursery Rhymes"),
          ("Ladybird Key Words Flashcards", "Flashcards", "Flashcards to practise common words.", "Ladybird Key Words flashcards"),
          ("Key Words with Peter and Jane: 2b Have a Go", "Reading scheme", "An early reading book.", "Key Words with Peter and Jane 2b Have a Go"),
          ("Key Words with Peter and Jane: 3a Things We Like", "Reading scheme", "A step up for early readers.", "Key Words with Peter and Jane 3a Things We Like")]
    page("best-ladybird-books-for-children", "Best Ladybird Books for Children | Tales and Key Words", "Best Ladybird books for children", "Ladybird books",
         "The best Ladybird books for children: fairy tales, nursery rhymes and Key Words with Peter and Jane reading books, with ages and links to buy on Amazon.ie.",
         "series-ladybird", "Two ladybirds on green leaves beside letter flashcards and an open book", "Classic Ladybird fairy tales, nursery rhymes and early reading books for young children.",
         "books-for-early-readers,books-for-preschoolers,best-nursery-rhyme-and-fairy-tale-books,how-to-read-aloud-to-children",
         "**Ladybird Books** is a long-established British children’s publisher, known for its small hardbacks, retold fairy tales and the Key Words with Peter and Jane reading scheme. Ladybird books suit children from about 2 to 7, depending on the title.",
         ["## Ladybird books for children", books(lb),
          "## Fairy tales and rhymes (ages 2 to 5)\n\nThe Ladybird Tales retell traditional stories in short, clear text. Pair them with nursery rhyme books for first story times. See our guide to [nursery rhyme and fairy tale books](/best-nursery-rhyme-and-fairy-tale-books/).",
          "## Early reading (ages 4 to 7)\n\nThe Key Words books and flashcards are designed to help children learn common words step by step. Use them alongside picture books and shared reading. See [books for early readers](/books-for-early-readers/).",
          "## Tips\n\n- Read the story together first, then let your child read the repeated words.\n- Keep sessions short and fun.\n- Check the level and age before you order."],
         [("What age are Ladybird books for?", "About 2 to 7, depending on the title. Tales and rhymes suit younger children, Key Words books suit early readers."),
          ("What is Key Words with Peter and Jane?", "A reading scheme from Ladybird that introduces common words in a series of graded books."),
          ("Are Ladybird Tales good for bedtime?", "Yes. They are short and suit reading aloud."),
          ("Where can I buy Ladybird books?", "Use the links on this page to check price and availability on Amazon.ie.")])
    # ---- Classic novels
    cn = [("Heidi", "By Johanna Spyri. Ages 8 and up", "A Swiss girl is sent to live with her grandfather in the Alps in this classic story. Spyri published it in 1880 and 1881.", "Heidi Johanna Spyri Puffin Classics"),
          ("Little Women", "By Louisa May Alcott, 1868 to 1869. Ages 9 and up", "The story of the four March sisters, Meg, Jo, Beth and Amy, growing up in America.", "Little Women Louisa May Alcott"),
          ("Anne of Green Gables", "By L.M. Montgomery, 1908. Ages 9 and up", "An imaginative orphan girl arrives on Prince Edward Island. [Read our guide](/anne-of-green-gables/).", "Anne of Green Gables L.M. Montgomery"),
          ("The Wind in the Willows", "By Kenneth Grahame, 1908. Ages 6 to 10", "Riverbank adventures with Mole, Ratty, Badger and Toad. [Read our guide](/the-wind-in-the-willows/).", "The Wind in the Willows Kenneth Grahame"),
          ("Alice’s Adventures in Wonderland", "By Lewis Carroll, 1865. Ages 7 and up", "A girl falls down a rabbit hole into a world of nonsense. [Read our guide](/alices-adventures-in-wonderland/).", "Alice's Adventures in Wonderland Lewis Carroll"),
          ("Charlie and the Chocolate Factory", "By Roald Dahl, 1964. Ages 6 to 10", "Five children win golden tickets to a chocolate factory. [Read our guide](/charlie-and-the-chocolate-factory/).", "Charlie and the Chocolate Factory Roald Dahl")]
    page("best-classic-childrens-novels", "Best Classic Children’s Novels | Heidi, Little Women", "Best classic children’s novels", "Classic children’s novels",
         "The best classic children’s novels, including Heidi, Little Women, Anne of Green Gables and Alice in Wonderland, with ages and where to buy.",
         "series-classic-novels", "A cottage beneath mountains with trees and an open book in a green meadow", "Heidi, Little Women, Anne and more: classics that are still loved by young readers.",
         "best-childrens-books-of-all-time,books-for-early-readers,how-to-read-aloud-to-children,anne-of-green-gables",
         "Classic novels are often best shared. Read a chapter at a time, or choose an abridged edition for younger children. These six classics suit readers from about 7 up, and each has stood the test of time.",
         ["## Classic children’s novels", books(cn),
          "## Tips for reading classics\n\n- **Start with a chapter.** Long books feel easier in small pieces.\n- **Choose a good edition.** Look for clear print and illustrations.\n- **Talk about old words.** Looking up a few words together can be fun.\n- **Try the audiobook.** Listen in the car and read the book at bedtime.",
          "## More classics\n\nSee our [best children’s books of all time](/best-childrens-books-of-all-time/) for 20 more."],
         [("What are the best classic children’s novels?", "Heidi, Little Women, Anne of Green Gables, The Wind in the Willows and Alice’s Adventures in Wonderland are among the most loved."),
          ("What age is Heidi for?", "About 8 and up as a solo read, or younger as a read-aloud."),
          ("What age is Little Women for?", "About 9 and up."),
          ("Are older novels hard to read?", "Some have old-fashioned language, so abridged editions or reading aloud can help.")])
    # ---- Nursery rhymes & fairy tales
    nr = [("Twinkle, Twinkle, Little Star", "Nursery rhyme", "The poem began as “The Star” by Jane Taylor, published in 1806, and is now sung to an older French tune.", "Twinkle Twinkle Little Star book"),
          ("Little Red Riding Hood", "Fairy tale", "A traditional tale retold by Charles Perrault in 1697 and later the Brothers Grimm.", "Little Red Riding Hood book"),
          ("The Enormous Turnip", "Folk tale", "A traditional tale about a turnip that will not budge.", "The Enormous Turnip Ladybird Tales"),
          ("The Magic Porridge Pot", "Folk tale", "A tale about a pot that makes porridge and cannot stop.", "The Magic Porridge Pot Ladybird Tales"),
          ("Goodnight Farm", "Board book", "A calm bedtime board book set on a farm.", "Goodnight Farm board book"),
          ("My Box of Bedtime Stories", "Box set", "A box of bedtime stories for the end of the day.", "My Box of Bedtime Stories")]
    page("best-nursery-rhyme-and-fairy-tale-books", "Best Nursery Rhyme and Fairy Tale Books for Kids", "Best nursery rhyme and fairy tale books", "Nursery rhymes and fairy tales",
         "The best nursery rhyme and fairy tale books for toddlers and preschoolers, including Twinkle Twinkle, Little Red Riding Hood and bedtime story boxes.",
         "series-nursery-fairy-tales", "A moonlit night with a cooking pot, a turnip and a basket under the stars", "Rhymes, folk tales and bedtime books to share with the youngest listeners.",
         "bedtime-stories-for-children,best-ladybird-books-for-children,books-for-preschoolers,how-to-read-aloud-to-children",
         "Nursery rhymes and fairy tales are the first stories many children hear. Rhyme and repetition help children learn the sounds of language, and the stories are short enough for bedtime. These books suit children from about 1 to 6.",
         ["## Nursery rhyme and fairy tale books", books(nr),
          "## Why nursery rhymes matter\n\nRhymes and songs help children hear the sounds in words, which supports later reading. Sing them, clap along and add actions.",
          "## Tips\n\n- Let your child fill in the last word of each line.\n- Add actions, such as twinkling fingers for the star.\n- Choose short fairy tales for toddlers and longer versions for older children.\n\nFor more, see our [bedtime stories guide](/bedtime-stories-for-children/) and [Ladybird books](/best-ladybird-books-for-children/)."],
         [("What are the best nursery rhyme books?", "Look for clear pictures, familiar rhymes and sturdy pages."),
          ("What age are fairy tales for?", "Short retellings suit ages 2 to 6. Longer versions suit older children."),
          ("Where does Twinkle Twinkle Little Star come from?", "The words come from a poem called The Star by Jane Taylor, published in 1806."),
          ("Are fairy tales too scary?", "Some have scary moments. Read them first and choose gentler versions if needed.")])
    print("wrote 8 series pages")


if __name__ == "__main__":
    main()
