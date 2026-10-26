# 指标口径

| 指标 | 定义 | 计算方式 |
| --- | --- | --- |
| 发送数 | 去重后的邮件触达次数 | `DISTINCTCOUNT(email_id)` |
| 打开数 | `opened = 1` 的邮件触达次数 | 按 `email_id` 去重 |
| 回复数 | `replied = 1` 的邮件触达次数 | 按 `email_id` 去重 |
| 完成跟进数 | `follow_up_completed = 1` 的邮件触达次数 | 按 `email_id` 去重 |
| 打开率 | 打开数 / 发送数 | `Open Users / Sent Users` |
| 回复率 | 回复数 / 发送数 | `Reply Users / Sent Users` |
| 打开后回复率 | 回复数 / 打开数 | `Reply Users / Open Users` |
| 跟进率 | 完成跟进数 / 发送数 | `Follow Up Users / Sent Users` |

## 漏斗校验规则

- `replied = 1` 时，`opened` 必须为 1。
- `follow_up_completed = 1` 时，`replied` 必须为 1。
- `email_id` 不应重复；重复记录应在数据质量页单独统计。
- 关键维度包括 `send_date`、`email_type`、`channel`、`region`、`device_type`、`user_segment`。
