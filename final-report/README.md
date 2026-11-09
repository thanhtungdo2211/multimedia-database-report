# AC5211 final report: LoRA + SDM on RSTPReid

A 6-page IEEE conference-format report (IEEEtran, English).

Author: Đỗ Thanh Tùng (20252432M)

## Build

```bash
cd final-report
python3 scripts/gen_results.py      # results/*.csv -> generated/numbers.tex + curve_*.csv
latexmk -pdf main.tex               # -> main.pdf
```

On Overleaf, upload the whole folder and use the pdfLaTeX compiler. `IEEEtran.cls` and `IEEEtran.bst` are bundled because the local TeX Live does not ship them.

## Where the numbers come from

| Source | Used for |
|---|---|
| `results/sdm_log.csv` | LoRA r=4 + SDM, centralized, 20 epochs (`master-thesis/data/runs/C1_true_centralized_lora4_20261309`) |
| `results/infonce_log.csv` | LoRA r=4 + InfoNCE, 30-epoch schedule, stopped at 27 (`C1_true_lora4_infonce`) |
| `results/mpce_log.csv` | LoRA r=4 + MPCE, 30 epochs (`C1_true_lora4_mpce`) |
| IRRA paper (arXiv 2303.12501), Tables 3–5 | The IRRA rows, typed in the `.tex` next to a citation |

Rule: the `.tex` files never hard-code a number from our own runs. They use the macros in `generated/numbers.tex`.

## Structure and "existing vs. ours"

| Section | Content | Tag |
|---|---|---|
| I. Introduction | Context: experiments drawn from the FL+PEFT thesis; goal = test the centralized premise "small update, little accuracy loss"; Q1/Q2, contributions, Table I (existing vs. ours) | – |
| II. Related work | TBPS, PETL, FedSH | – |
| III. Background | CLIP, SDM, IRRA ablation | **[Existing]** |
| IV. Method and analysis | LoRA setup; in-batch positive rate (1.52%); SDM = λ·MAE − H(p); gradient; MPCE control | **[Ours]** |
| V. Experiments | Table II (vs. IRRA), Table III + Fig. 2 (loss ablation), Table IV (FL cost accounting: K=15 clients, R=30 rounds, arithmetic only) | **[Ours]** |
| VI–VII | Limitations, conclusion | – |

## Plan / status

- [x] E2 loss ablation: InfoNCE, MPCE
- [x] Report skeleton, generated numbers, figures, tables, bibliography (DOI/arXiv via `fetch_bibtex.sh` or copied from `master-thesis/paper/refs.bib`)
- [x] Full draft, 6 pages, compiles without errors or overfull boxes
- [ ] (optional) SDM rerun with `--rounds 30` so all three losses share one LR schedule. This removes the caveat in Sec. V-A/VI.
- [ ] (optional) Second seed for SDM.
- [ ] Author proofread; add the university/faculty name to the author block if required.

Scope note: no federated run is reported (the FedAvg r=4/r=8 runs stay in the thesis). Only the three centralized loss runs are used.
