#!/usr/bin/env python3
"""Generate every experimental number used in the report from results/*.csv.

Writes
  generated/numbers.tex    LaTeX macros (\\sdmPeakR, \\nceConvR, ...)
  generated/curve_<loss>.csv  epoch-wise R@1 / mAP for the pgfplots figure

Rule: the .tex sources never hard-code a number from our own runs; they use these
macros. Numbers quoted from the IRRA paper are typed in the .tex with a citation.

Run from final-report/:  python3 scripts/gen_results.py
"""
import csv
import json
import math
import os
import statistics as st

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")
GEN = os.path.join(HERE, "generated")
os.makedirs(GEN, exist_ok=True)

METRICS = ["R@1", "R@5", "R@10", "mAP", "mINP"]
MNAME = {"R@1": "R", "R@5": "Rfive", "R@10": "Rten", "mAP": "M", "mINP": "MINP"}
LAST_K = 6  # "converged" = mean of the last 6 evaluated epochs (same rule as the thesis)
N_ID_TRAIN = 3701  # RSTPReid training identities (matches partition_stats.json)


def load(name):
    with open(os.path.join(RES, f"{name}_log.csv")) as f:
        rows = [r for r in csv.DictReader(f) if r["R@1"]]
    for r in rows:
        for k in list(r):
            if r[k] != "":
                r[k] = float(r[k])
    return rows


def args(name):
    with open(os.path.join(RES, f"{name}_args.json")) as f:
        return json.load(f)


macros = {}


def put(key, val, nd=2):
    macros[key] = f"{val:.{nd}f}" if isinstance(val, float) else str(val)


# ---------------- centralized loss ablation ----------------
runs = {"sdm": load("sdm"), "mpce": load("mpce"), "nce": load("infonce")}
for tag, rows in runs.items():
    peak = max(rows, key=lambda r: r["R@1"])
    put(f"{tag}PeakEp", int(peak["round"]))
    for m in METRICS:
        put(f"{tag}Peak{MNAME[m]}", peak[m])
    bm = max(rows, key=lambda r: r["mAP"])
    put(f"{tag}BestM", bm["mAP"])
    put(f"{tag}BestMEp", int(bm["round"]))
    tail = rows[-LAST_K:]
    put(f"{tag}ConvR", st.mean(r["R@1"] for r in tail))
    put(f"{tag}ConvRsd", st.stdev(r["R@1"] for r in tail))
    put(f"{tag}ConvM", st.mean(r["mAP"] for r in tail))
    put(f"{tag}ConvMsd", st.stdev(r["mAP"] for r in tail))
    put(f"{tag}Epochs", int(rows[-1]["round"]))
    put(f"{tag}LastR", rows[-1]["R@1"])
    put(f"{tag}Drop", peak["R@1"] - rows[-1]["R@1"])
    put(f"{tag}LossFirst", rows[0]["loss"])
    put(f"{tag}LossLast", rows[-1]["loss"])
    by_ep = {int(r["round"]): r for r in rows}
    put(f"{tag}EpNineR", by_ep[9]["R@1"])
    put(f"{tag}EpFourR", by_ep[4]["R@1"])
    put(f"{tag}EpThreeR", by_ep[3]["R@1"])
    # epoch-wise curve for pgfplots
    with open(os.path.join(GEN, f"curve_{tag}.csv"), "w") as f:
        f.write("epoch,r1,map\n")
        for r in rows:
            f.write(f"{int(r['round'])},{r['R@1']:.2f},{r['mAP']:.2f}\n")
    # wall-clock per epoch
    el = [r["elapsed_s"] for r in rows]
    put(f"{tag}MinPerEp", (el[-1] - el[0]) / (len(el) - 1) / 60, 1)

# gaps at the peak
put("gapSdmNceR", float(macros["sdmPeakR"]) - float(macros["ncePeakR"]))
put("gapSdmNceM", float(macros["sdmPeakM"]) - float(macros["ncePeakM"]))
put("gapSdmMpceR", float(macros["sdmPeakR"]) - float(macros["mpcePeakR"]))
put("gapSdmMpceM", float(macros["sdmPeakM"]) - float(macros["mpcePeakM"]))
put("gapSdmMpceBestM", float(macros["sdmBestM"]) - float(macros["mpceBestM"]))

# mpce vs infonce, epoch by epoch (same 30-epoch schedule)
pairs = list(zip(runs["mpce"], runs["nce"]))
assert all(a["round"] == b["round"] and a["lr"] == b["lr"] for a, b in pairs), "schedules differ"
dR = [a["R@1"] - b["R@1"] for a, b in pairs]
dM = [a["mAP"] - b["mAP"] for a, b in pairs]
put("mpNceDiffR", st.mean(dR))
put("mpNceDiffRsd", st.stdev(dR))
put("mpNceDiffRmax", max(map(abs, dR)))
put("mpNceDiffM", st.mean(dM))
put("mpNceDiffMmax", max(map(abs, dM)))
ratio = [a["loss"] / b["loss"] for a, b in pairs]
put("lossRatioLo", min(ratio))
put("lossRatioHi", max(ratio))
put("nPairedEp", len(pairs))

# learning rates over epochs 4..9 (shows the schedule mismatch is small there)
for tag in ("sdm", "nce"):
    by_ep = {int(r["round"]): r for r in runs[tag]}
    put(f"{tag}LrFour", f"{by_ep[4]['lr'] * 1e5:.2f}")
    put(f"{tag}LrNine", f"{by_ep[9]['lr'] * 1e5:.2f}")

s_ep = {int(r["round"]): r["lr"] for r in runs["sdm"]}
n_ep = {int(r["round"]): r["lr"] for r in runs["nce"]}
put("lrMaxRelDiff", 100 * max(abs(s_ep[e] - n_ep[e]) / max(s_ep[e], n_ep[e]) for e in range(4, 10)), 0)
# gaps to IRRA's published numbers (Table 3 / Table 4 of the IRRA paper)
IRRA_FULL_R, IRRA_FULL_M, IRRA_SDM_R, IRRA_NCE_R = 60.20, 47.17, 57.20, 54.05
put("gapIrraR", IRRA_FULL_R - float(macros["sdmPeakR"]))
put("gapIrraM", IRRA_FULL_M - float(macros["sdmPeakM"]))
put("gapIrraSdmR", float(macros["sdmPeakR"]) - IRRA_SDM_R)
put("gainIrraSdm", IRRA_SDM_R - IRRA_NCE_R)

# ---------------- model size ----------------
a = args("sdm")
for t in ("mpce", "infonce"):
    b = args(t)
    assert all(a[k] == b[k] for k in ("lora_rank", "lora_alpha", "lr", "batch_size", "seed",
                                      "temperature", "trainable_params")), t
put("nTrainable", f"{a['trainable_params']:,}".replace(",", "\\,"))
put("nTotal", f"{a['total_params']:,}".replace(",", "\\,"))
backbone = a["total_params"] - a["trainable_params"]  # frozen CLIP = what full FT would train
put("nTotalM", a["total_params"] / 1e6, 1)
put("nBackbone", f"{backbone:,}".replace(",", "\\,"))
put("nBackboneM", backbone / 1e6, 1)
put("trainPct", 100 * a["trainable_params"] / a["total_params"])
put("nLoraModules", a["n_lora_modules"])
put("ckptMiB", a["trainable_params"] * 4 / 2**20, 2)
put("fullMiB", backbone * 4 / 2**20, 0)
put("sizeRatio", backbone / a["trainable_params"], 0)
put("idHeadM", (512 * N_ID_TRAIN + N_ID_TRAIN) / 1e6, 2)  # IRRA ID head: Linear(512, #train IDs)
put("batchSize", a["batch_size"])
put("sdmRounds", a["rounds"])
put("nceRounds", args("infonce")["rounds"])
put("mpceRounds", args("mpce")["rounds"])

# ---------------- in-batch positives ----------------
# RSTPReid train: 3,701 identities x 5 images x 2 captions = 37,010 (image, caption)
# examples; shuffle=True sampling. Probability that a row of a B-row batch has at least
# one other example of its identity (i.e., the SDM label row is not one-hot).
N_ID, PER_ID, B = 3701, 10, a["batch_size"]
N = N_ID * PER_ID
p_none = 1.0
for j in range(B - 1):
    p_none *= (N - PER_ID - j) / (N - 1 - j)
put("posFrac", 100 * (1 - p_none))
put("oneHotFrac", 100 * p_none)
put("nExamples", f"{N:,}".replace(",", "\\,"))
put("logInvEps", math.log(1e8))

# ---------------- federated cost accounting (arithmetic, not a measurement) ----------------
# K = 15 clients (one per RSTPReid camera), R = 30 rounds, fp32 parameters. Each client uploads
# its trainable parameters once per round; AdamW keeps two fp32 moments per trainable parameter.
K_CLIENTS, R_ROUNDS = 15, 30
MiB, GiB = 2**20, 2**30
lora_b, full_b = a["trainable_params"] * 4, backbone * 4
put("kClients", K_CLIENTS)
put("rRounds", R_ROUNDS)
put("upLoraRoundMiB", K_CLIENTS * lora_b / MiB, 1)
put("upFullRoundGiB", K_CLIENTS * full_b / GiB, 1)
put("upLoraTotalGiB", K_CLIENTS * R_ROUNDS * lora_b / GiB, 2)
put("upFullTotalGiB", K_CLIENTS * R_ROUNDS * full_b / GiB, 0)
put("optLoraMiB", 2 * lora_b / MiB, 2)
put("optFullGiB", 2 * full_b / GiB, 2)
put("roundVsOneFull", full_b / (K_CLIENTS * lora_b), 0)

with open(os.path.join(GEN, "numbers.tex"), "w") as f:
    f.write("% AUTO-GENERATED by scripts/gen_results.py -- do not edit by hand.\n")
    for k, v in macros.items():
        f.write(f"\\newcommand{{\\{k}}}{{{v}}}\n")
print(f"wrote {len(macros)} macros to generated/numbers.tex")
for k in ("sdmPeakR", "mpcePeakR", "ncePeakR", "posFrac", "mpNceDiffR", "lossRatioLo", "lossRatioHi",
          "sdmConvR", "nceConvR", "mpceConvR", "ckptMiB", "fullMiB", "sizeRatio", "trainPct"):
    print(f"  {k} = {macros[k]}")
