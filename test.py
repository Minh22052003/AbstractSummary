from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the pre-trained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("./bart_summarization_model")
model = AutoModelForSeq2SeqLM.from_pretrained("./bart_summarization_model")

def summarize(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
    
    # Decode the summary tokens back into text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

# Tóm tắt văn bản
text = """ Các chuyên gia hàng không lo ngại một hành động cố ý đã khiến máy bay biến mất khỏi màn hình radar vào sáng ngày 19.5, theo tờ South China Morning Post (Hồng Kông) ngày 20.5.
Bộ Ngoại giao Ai Cập cho hay các vật thể trôi trên mặt biển được tìm thấy gần đảo Karpathos, Hy Lạp có thể là của máy bay Airbus A320, hãng EgyptAir cho hay trên Twitter. Nhưng ông Athanasios Binis, Chủ tịch Ủy ban An toàn và Điều tra Tai nạn Hàng không Hy Lạp, nói mảnh vỡ, bao gồm áo cứu sinh và các mảnh nhựa, là không phải của chiếc Airbus A320.
Sau đó, Phó chủ tịch EgyptAir, Ahmed Adel thừa nhận EgyptAir đưa ra thông tin sai và “công tác tìm kiếm và cứu hộ đang diễn ra”.
“Tổng thống Ai Cập Abdel Fattah al-Sisi ra lệnh cho các cơ quan hữu trách, bao gồm Bộ Hàng không dân dụng, lực lượng không quân và hải quân tăng cường công tác tìm kiếm máy bay và áp dụng mọi biện pháp cần thiết để tìm ra mảnh vỡ máy bay”, theo thông cáo từ văn phòng Tổng thống Ai Cập. Mỹ, Pháp, Hy Lạp cũng phối hợp với Ai Cập tìm kiếm máy bay và điều tra vụ việc.
Chiếc Airbus A320 (chuyến bay số hiệu MS804), chở theo 66 người, bay từ thủ đô Paris (Pháp) đến thủ đô Cairo (Ai Cập) thì biến mất khỏi màn hình radar vào sáng sớm ngày 19.5. Hãng EgyptAir cho hay máy bay mất liên lạc với mặt đất khi cách bờ biển phía bắc Ai Cập khoảng 280 km và không phát tín hiệu cầu cứu, theo ông Adel.
Theo Bộ trưởng Hàng không Dân dụng Ai Cập Sherif Fathi, hiện còn quá sớm để có thể kết luận vì sao chiếc Airbus A320 biến mất, nhưng khả năng đây là “một vụ khủng bố” cao hơn là máy bay bị sự cố kỹ thuật. Còn Tổng thống Pháp Francois Hollande xác nhận máy bay này đã rơi ở Địa Trung Hải.
Tổng thống Sisi cũng ra lệnh cho Bộ Hàng không Dân dụng Ai Cập lập ủy ban lập tức tiến hành điều tra nguyên nhân vì sao máy bay EgyptAir mất tích.
Các điều tra viên đang xem xét cả khả năng máy bay rơi do bom, theo AFP. Trong khi đó, các quan chức từ nhiều cơ quan của chính phủ Mỹ cho Reuters biết dựa theo phân tích hình ảnh vệ tinh, cho đến nay vẫn chưa phát hiện bất kỳ dấu hiệu nào cho thấy máy bay của EgyptAir phát nổ trong không trung.
Tại sân bay quốc tế Cairo (Ai Cập), một người đàn ông ôm mặt khóc và nói: “Ai Cập sẽ còn tồn tại được bao lâu khi mạng người quá rẻ rúng?”.
Mẹ của một tiếp viên hàng không trên chiếc máy bay mất tích chạy đến sân bay Cairo, nơi gia đình các nạn nhân ngóng trông tin tức người thân từng giờ từng phút. Bà cho biết lần cuối cùng con gái gọi điện thoại cho bà là vào tối 18.5. “Chính quyền chẳng thông báo cho chúng tôi biết bất kỳ điều gì”, người mẹ bức xúc nói.
Một số thân nhân hành khách định xông tới đánh một người chụp ảnh của EgyptAir. Người này định chụp một số ảnh về thân nhân hành khách và lực lượng an ninh sân bay buộc phải đưa anh ta ra khỏi khu vực tập trung các thân nhân."""
print("Tóm tắt:", summarize(text))
