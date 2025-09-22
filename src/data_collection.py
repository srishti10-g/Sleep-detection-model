from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import time, random, os

def scrape_images(engine, query, save_dir, num=1500, min_size=(500, 500)):
    if engine == "google":
        crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
    elif engine == "bing":
        crawler = BingImageCrawler(storage={"root_dir": save_dir})
    else:
        raise ValueError("Engine must be 'google' or 'bing'")

    crawler.crawl(keyword=query, max_num=num, min_size=min_size, file_idx_offset=0)

if __name__ == "__main__":
    queries = {
        "sleeping": [
            "security guard sleeping at night",
            "man sleeping on chair in uniform",
            "watchman sleeping on duty",
            "night watchman asleep on chair",
            "exhausted guard falling asleep",
            "sleeping person",
            "watchman sleepy laying",
            "human laying on chair",
        ],
        "awake": [
            "security guard awake on duty",
            "alert watchman at night",
            "guard standing watch",
            "security guard monitoring cctv",
            "watchman checking surroundings",
            "guard walking at night",
            "alert man with uniform on duty",
            "security guard observing carefully",
            "human awake with open eyes",
        ]
    }

    for category, qlist in queries.items():
        for q in qlist:
            save_dir = f"data/raw/{category}/{q.replace(' ', '_')}_{int(time.time())}"
            os.makedirs(save_dir, exist_ok=True)
            print(f"\n Downloading {category} -> {q}")

            for engine in ["google", "bing"]:
                scrape_images(engine, q, save_dir, num=500, min_size=(500, 500))
                sleep_time = random.randint(3, 7)
                print(f" Sleeping {sleep_time} sec...")
                time.sleep(sleep_time)

            time.sleep(random.randint(5, 10))

    print("\n✅ All downloads completed! Check 'data/raw'.")
