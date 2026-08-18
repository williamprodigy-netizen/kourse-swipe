#!/usr/bin/env python3
"""Build the PB Trading swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/KOURSE_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {}

CONFIG = {
 "SITE": "Max Perzon — Kourse",
 "CREATOR": "Max Perzon",
 "ADS_KEY": "kourse",
 "FUNNEL_IDS": ["F053"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/KOURSE_Swipe",
 "BLURB": "Teaching people to sell courses on Skool. Every email is <b>one minute long</b> and every "
          "one is <b>mirrored as a Skool post</b> &mdash; one asset, two distribution channels.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Vehicle","Skool communities"),("Headline claim","$230,758/month in 30 days"),
           ("Player","<b>Loom</b>, not a VSL player"),("Emails captured","11"),
           ("Email length","&ldquo;Read time: 1 minute&rdquo;"),
           ("Promo","33% off · 100 spots · ends 31 Aug"),
           ("CRM","GoHighLevel"),("Free front end","Skool: &ldquo;Free Skool Course&rdquo;")],
 "OFFER": [("Product","Kourse &mdash; building and selling a course on Skool"),
   ("Headline","&ldquo;How I Built a <b>$230,758/month</b> Online Course In 30 days&rdquo;"),
   ("Authority","Entered Alex Hormozi's Skool Games and &ldquo;walked away with a <b>$100K check from him personally</b>&rdquo;"),
   ("Free front end","A free Skool community, plus a recurring <b>live masterclass</b>"),
   ("Promo","33% off, <b>1-on-1 success coach</b>, 100 spots, ends 31 August"),
   ("Path","Ads / organic &rarr; free Skool group &rarr; 1-min emails + mirrored posts &rarr; live masterclass &rarr; Kourse"),
   ("Price","<b>Not stated</b> on the start page &mdash; only the 33% discount is named")],
 "FINDINGS": [
  ("Every email is also a Skool post, same day, same copy",
   "&ldquo;I speedran a Skool from 0 to $231k/month in 30 days&rdquo; went out from "
   "<code>max@kourse.com</code> on 21 July and posted to his free Skool community the same morning. "
   "Same for &ldquo;Alex Hormozi's Skool Strategy for 2026&rdquo; (27 July), &ldquo;The NEW Rules of "
   "Selling Courses&rdquo; (9 July) and the rest. <b>One asset, two channels, plus Skool's own weekly "
   "digest re-mailing it a third time.</b> He writes once and lands three times."),
  ("Every email opens with its own read time",
   "<b>&ldquo;Read time: 1 minute&rdquo;</b> is the first line of nearly every send. It removes the "
   "only real objection to opening a marketing email, and it is a promise he then has to keep &mdash; "
   "which keeps the emails genuinely short. <span class=\"tag good\">worth stealing</span>"),
  ("The headline number is not rounded",
   "<b>$230,758/month</b>, not &ldquo;$230k&rdquo;. Sometimes written $231k in the emails. An exact "
   "figure reads as pulled from a dashboard; a round one reads as a claim. Same instinct as PB "
   "Trading's &ldquo;862 days in a row&rdquo;."),
  ("He borrows Hormozi's authority with a receipt, not a name-drop",
   "&ldquo;I entered Alex Hormozi's Skool Games after building a $230K/month course business in 30 "
   "days. <b>Walked away with a $100K check from him personally.</b>&rdquo; The check is the proof; "
   "Hormozi is the witness. Four of the eleven captured emails are built on Hormozi's name."),
  ("The offer's second half is the interesting half",
   "The promo is not just 33% off &mdash; it is 33% off <b>plus a dedicated 1-on-1 success coach</b>, "
   "and one email exists purely to explain <i>why that second part matters more than the discount</i>. "
   "He discounts the price and then argues the reader should care about the service instead."),
  ("A segmented email that says so out loud",
   "6 July: <i>&ldquo;Quick one, this email is <b>only going to current Kourse customers</b>, not our "
   "full list.&rdquo;</i> Naming the segment inside the email makes the reader feel selected. Whether "
   "the segmentation was real is not verifiable from the inbox."),
 ],
 "FUNNEL": [
  ("Start page","kourse.com/start",'&ldquo;How I built a $230,758/month online course in 30 days.&rdquo; <b>Loom</b> embeds, named testimonials. Meta Pixel + GA + Clarity + GoHighLevel.'),
  ("Free Skool group","skool.com — &ldquo;Free Skool Course&rdquo;",'<span class="tag good">the engine</span> Every email mirrored here as a post. Skool then re-mails it in the weekly digest.'),
  ("Live masterclass","Skool event",'&ldquo;Learn how to enter the $250 Billion online education industry.&rdquo; Recurring, Saturday mornings LA time.'),
  ("Email","max@kourse.com","11 captured in Will's personal inbox, 6 July &ndash; 4 Aug. Every one opens &ldquo;Read time: 1 minute&rdquo;."),
 ],
 "TRANSCRIPT_GROUPS": [],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>The distribution trick is the lesson, not the offer.</b> Max writes one short
piece and it lands three times: as an email from his own domain, as a post in his free Skool group,
and again inside Skool's automated weekly digest. Three impressions, one piece of writing.</div>

<h2 class="sec">The captured sequence</h2>
<div class="tablewrap"><table>
<tr><th>Date</th><th>Subject</th><th>Job</th></tr>
<tr><td>6 Jul</td><td>A note for current Kourse customers only</td><td>Segment flattery + launch the coach</td></tr>
<tr><td>7 Jul</td><td>Alex Hormozi's Advice on Selling Courses</td><td>Borrowed authority + the $100K check</td></tr>
<tr><td>8 Jul</td><td>Just launched something NEW! 100 spots. Ends August 31st.</td><td>Open the promo</td></tr>
<tr><td>9 Jul</td><td>33% Discount. 1-on-1 Success Coach. 100 Spots.</td><td>Argue the coach &gt; the discount</td></tr>
<tr><td>9 Jul</td><td>The NEW Rules of Selling Courses (2026)</td><td>Value</td></tr>
<tr><td>10 Jul</td><td>Craziest offer I've ever done...!</td><td>&ldquo;Third and final in this series&rdquo;</td></tr>
<tr><td>13 Jul</td><td>Everything I Learned From Alex Hormozi &amp; Sam Ovens</td><td>Value + authority</td></tr>
<tr><td>14 Jul</td><td>He joined 90 days ago &amp; just hit his first $30k month</td><td>Student proof, dated and named</td></tr>
<tr><td>21 Jul</td><td>I speedran a new Skool from 0 to $231k/month in 30 days</td><td>Operator proof</td></tr>
<tr><td>27 Jul</td><td>Alex Hormozi's Skool Strategy for 2026</td><td>Authority</td></tr>
<tr><td>30 Jul</td><td>How To Create a Course SO Premium They Beg To Buy</td><td>Value</td></tr>
</table></div>
<p style="margin-top:12px">The promo runs as a <b>banner inside every email</b> rather than as
dedicated pitch sends &mdash; &ldquo;quick heads up, 33% off is live&rdquo; sits above value content
for four straight weeks. The deadline never moves, so the urgency stays honest.</p>

<h2 class="sec">The student-proof email is the best one</h2>
<p><i>&ldquo;Daniel joined Kourse on <b>April 27</b>. He wrote down one goal that day. &lsquo;My first
$30k month will be in July.&rsquo; I just saw his mid July update, not even 90 days later&hellip;
$30,000.&rdquo;</i></p>
<p>A dated join, a written goal quoted verbatim, and the outcome landing on the date the student
themselves predicted. The proof is the <i>prediction being kept</i>, not the number. That structure is
directly available to us &mdash; our students write goals on day one and we never quote them back.</p>

<h2 class="sec">Where the emails actually were</h2>
<p><span class="tag">EVIDENCE</span> Not in the research inbox. All 11 are in <b>Will's personal
Gmail</b> (williamprodigy@gmail.com), from <code>max@kourse.com</code>. The underground archive holds
930 messages and <b>zero</b> mention Perzon or Kourse &mdash; the research account is a member of
Will's own Skool groups, not Max's.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>The thank-you page and post-optin sequence.</b> Will asked for the TY-page emails
specifically; what exists in the inbox is the ongoing broadcast list, not a triggered welcome flow.
Capturing that needs a real opt-in at kourse.com/start.</li>
<li><b>No price.</b> Only the 33% discount is ever named.</li>
<li><b>The Loom videos on the start page are identified but not pulled.</b></li>
<li><b>No ads found</b> under kourse.com in the ad index.</li></ul>
""",
}
CONFIG['VIDEOS'] = video_library()

if __name__ == '__main__':
    build(CONFIG)
