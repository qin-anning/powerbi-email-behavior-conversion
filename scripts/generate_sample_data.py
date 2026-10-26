"""Generate reproducible course-project sample data for the Power BI dashboard."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20261026)
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "email_behavior_sample.csv"

regions = ["China", "Singapore", "Malaysia", "Thailand"]
channels = ["Organic", "Paid search", "Referral", "Campus"]
devices = ["Mobile", "Desktop", "Tablet"]
segments = ["New", "Returning", "High intent"]

with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
    fields = ["email_id", "user_id", "send_date", "send_week", "email_type", "channel", "region", "device_type", "user_segment", "opened", "replied", "follow_up_completed"]
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    start_date = date(2026, 3, 2)
    for index in range(1, 481):
        sent = start_date + timedelta(days=random.randrange(56))
        email_type = "AI assisted" if index % 2 == 0 else "Manual"
        channel, segment = random.choice(channels), random.choice(segments)
        open_probability = 0.38 + (0.05 if email_type == "AI assisted" else 0) + (0.04 if channel == "Referral" else 0) + (0.03 if segment == "Returning" else 0)
        opened = int(random.random() < open_probability)
        replied = int(opened and random.random() < 0.16 + (0.03 if email_type == "AI assisted" else 0))
        followed_up = int(replied and random.random() < 0.36 + (0.04 if segment == "High intent" else 0))
        writer.writerow({
            "email_id": f"EML-{index:04d}", "user_id": f"USR-{random.randrange(1, 321):04d}",
            "send_date": sent.isoformat(), "send_week": sent.strftime("%G-W%V"),
            "email_type": email_type, "channel": channel, "region": random.choice(regions),
            "device_type": random.choices(devices, weights=[0.62, 0.30, 0.08])[0],
            "user_segment": segment, "opened": opened, "replied": replied,
            "follow_up_completed": followed_up,
        })
