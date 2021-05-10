library('tidyverse');

# Day vs text count
ggplot(data=daily_text_count, aes(x=date,y=n)) + 
  ggtitle("Number of Texts by date") +
  geom_bar(stat="identity", fill="steelblue")

# time vs text count
ggplot(data=text_stats, aes(x=time)) + 
  ggtitle("Number of Texts by Time of Day") +
  geom_histogram(fill="steelblue",color="white") + 
  scale_x_datetime(date_label = "%H:%M")

# top 10 user frequency
ggplot(data=top_ten_sender_data, aes(x=time,color=sender)) +
  ggtitle("Texts sent vs time of day", subtitle="Top 10 most active members only") +
  geom_density() +
  scale_x_datetime(date_label = "%H:%M")

