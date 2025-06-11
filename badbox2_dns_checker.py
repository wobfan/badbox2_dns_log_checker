
import csv
from collections import defaultdict

NEXTDNS_LOG_FILE_NAME = "XXXXXX.csv"


def search_csv(filename, search_terms):
    results = defaultdict(list)

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row_idx, row in enumerate(reader):
            if row_idx % 100 == 0:
                print(f"Progress: Processing row {row_idx}...")

            for col_idx, cell in enumerate(row):
                for term in search_terms:
                    if term.lower() in cell.lower():
                        results[term].append((row_idx, col_idx))
                        print(f"✓ Found '{term}' at row {row_idx}, column {col_idx}")

    print(f"\nCompleted! Processed {row_idx + 1} rows.")
    return results


# c2 domains (source: https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/)
search_terms = ["100ulife.com", "coslogdydy.in", "ipmoyu.com", "pcxrlback.com", "tuding.xyz", "1ztop.work", "cxlcyy.com", "jasmine.land", "petrel-ip.com", "tvsnapp.com", "99soya.shop", "cxzyr.com", "jolted.vip", "pixelscast.com", "veezy.site", "ad3g.com", "dazzl.vip", "joyfulxx.com", "pixlo.cc", "vividweb.work", "admoyu.com", "dc16888888.com", "jutux.work", "pm2za.cc", "wildpettykiwi.com", "ads-goal.com", "dcylog.com", "logcer.com", "qazwsxedc.xyz", "wildpettykiwi.info", "ai-goal.com", "dqmop.com", "long.tv", "qocoll.com", "wildpettykiwi.xyz", "apotube.com", "duoduodev.com", "meiboot.com", "qulogger.com", "wotads.com", "app-goal.com", "easyjoy.me", "moonhub.work", "randomhow.com", "ycxad.com", "appclicking.com", "echojoy.xyz", "motiyu.net", "retrofitxer.com", "ycxrl.com", "astrolink.cn", "finemob.com", "moyix.com", "rzless.work", "ycxrldow.com",
                "bitemores.com", "firehub.link", "moyu88.xyz", "shanhulan.cn", "yeyeyeye.xyz", "bltproxy.com", "firehub.work", "msohu.online", "simplekds.me", "yxcrl.com", "bluefish.work", "flyermobi.com", "msohu.shop", "soyatea.online", "yydsma.com", "bullet-proxy.com", "fuhidd.com", "mtcpmpm.com", "sparkjoy.cc", "yydsmb.com", "catmore88.com", "g1ee.com", "mtcprogram.com", "supportdatainput.top", "yydsmd.com", "catmos99.com", "giddy.cc", "mtcpuouo.com", "sustat.com", "yydsmr.com", "cbphe.com", "goologer.com", "mymoyu.shop", "swiftcode.work", "ziyemy.shop", "cbpheback.com", "heygames.club", "navnow.xyz", "syloger.com", "ztword.com", "clickby.net", "huulog.com", "net-goal.com", "sysbinder.com", "zxcvbnmasdfghjkl.xyz", "clocksyn.com", "huuww.com", "pccyy.com", "sysbinder.xyz", "vmud.net", "ipforyou.top", "pcxrl.com", "ttyunos.com", "meisvip.com"]
results = search_csv(NEXTDNS_LOG_FILE_NAME, search_terms)

print("\n=== Summary ===")
for term, locations in results.items():
    print(f"'{term}': found {len(locations)} times")
