import streamlit as st
import segno
import io
import time
import hashlib # for generating dynamic tokens  
from streamlit_autorefresh import st_autorefresh


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    st_autorefresh(interval=1000, key="qr_timer")
    app_domain = "snapclass-ai-new.streamlit.app"

    st.header("Scan to Join")

    # Changes every 10 seconds
    current_slot = int(time.time() // 10)

    token = hashlib.md5(
        f"{subject_code}_{current_slot}".encode()
    ).hexdigest()[:10]

    join_url = (
        f"https://{app_domain}"
        f"/?join-code={subject_code}"
        f"&token={token}"
    )

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(
        out,
        kind="png",
        scale=10,
        border=1
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url)
        st.code(token)
        st.info("This QR refreshes every 10 seconds")

    with col2:
        st.markdown("### Scan To Join")
        st.image(
            out.getvalue(),
            caption="Dynamic Attendance QR"
        )

    st.caption(
        f"QR expires in {10 - (int(time.time()) % 10)} seconds"
    )

  