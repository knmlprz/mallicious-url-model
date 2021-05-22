import pandas as pd
import matplotlib.pyplot as plt


def prepare_good_links():
    alexdf = pd.read_csv('data/top50-alexa.csv', delimiter=';')
    mozdf = pd.read_csv('data/top500-Moz.csv', delimiter=',')
    poldf = pd.read_csv('data/top100-polska.csv', delimiter=',', index_col=0)
    govdf = pd.read_csv('data/wykaz-stron-gov.csv', delimiter=';')

    alexdf.columns = ["site_name", "domain", "description", "country"]
    alexdf.set_index(keys="domain", inplace=True)
    mozdf.drop(labels=["Rank", "Domain Authority"],
               axis='columns',
               inplace=True)
    mozdf.columns = ["domain", "linking_domains"]
    mozdf.set_index(keys="domain", inplace=True)
    alexdf = alexdf.merge(mozdf, on="domain", how="left")
    poldf.columns = ["description", "domain"]
    poldf.set_index(keys="domain", inplace=True)
    govdf.columns = ["description", "domain"]
    govdf.set_index(keys="domain", inplace=True)

    all_good_links = pd.concat([alexdf, mozdf, poldf], axis=0)
    resdf = all_good_links.loc[all_good_links.index.drop_duplicates().dropna()]
    resdf.reset_index(inplace=True)
    resdf = resdf[resdf.domain.apply(
        lambda domain: ' ' not in domain and '@' not in domain)]
    del all_good_links, mozdf, alexdf, poldf, govdf
    return resdf


def prepare_malware_links():
    baddf = pd.read_json('data/domains.json')
    fishdf = pd.read_csv('https://openphish.com/feed.txt', delimiter=' ',
                         header=None)
    baddf.columns = ["reg_pos_id", "domain", "insert_date", 'delete_date']
    baddf.set_index(keys="domain", inplace=True)
    fishdf.columns = ["domain"]
    fishdf.set_index(keys="domain", inplace=True)
    resdf = pd.concat([baddf, fishdf], axis=0)
    resdf = resdf.loc[resdf.index.drop_duplicates().dropna()]
    resdf.reset_index(inplace=True)
    del baddf, fishdf
    return resdf


def count_special_symbols(domain):
    counter = 0
    for char in domain:
        if char.isalpha() or char.isdigit():
            continue
        else:
            counter += 1
    return counter


def count_digits(domain):
    counter = 0
    for char in domain:
        if char.isdigit():
            counter += 1
    return counter


def domain_stats(domain_df):
    domain_df['spec_symb'] = domain_df["domain"].apply(count_special_symbols)
    domain_df['digits'] = domain_df["domain"].apply(count_digits)
    domain_df['length'] = domain_df["domain"].apply(len)

    domain_df['spec_symb_ratio'] = domain_df.spec_symb / domain_df.length
    domain_df['digits_ratio'] = domain_df.digits / domain_df.length
    return domain_df


# undf = pd.read_csv('data/unique_good_links.csv', index_col=0)
undf = prepare_good_links()
undf = domain_stats(undf)
badundf = pd.read_csv('data/unique_bad_links.csv', index_col=0)


undf = domain_stats(undf)
badundf = domain_stats(badundf)

fig, ax = plt.subplots(2, 2, sharex='col')
# ax[0, 0].set_xlim(left=0, right=3)
ax[0, 0].set_title("good-digits")
ax[0, 0].hist(undf.digits_ratio,
              # bins=10,
              label='good',
              color='green',
              alpha=0.5)
# ax[1, 0].set_xlim(left=0, right=10)
ax[1, 0].set_title("bad-digits")
ax[1, 0].hist(badundf.digits_ratio[1::23],
              bins=10,
              label='bad',
              color='red',
              alpha=0.5)
# ax[0, 1].set_xlim(left=3, right=25)
ax[0, 1].set_title("good-length")
ax[0, 1].hist(undf.length,
              # bins=10,
              label='good',
              color='green',
              alpha=0.5)
ax[1, 1].set_xlim(left=3, right=50)
ax[1, 1].set_title("bad-length")
ax[1, 1].hist(badundf.length[1::23],
              bins=100,
              label='bad',
              color='red',
              alpha=0.5)
plt.show()
