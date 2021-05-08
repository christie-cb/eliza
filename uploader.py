from bot import ElizaBot
from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py.deployment import advertise_deployed_bot

DEVELOPER_UID = "HMWa6BM9LbPgxZ8jiufxjeyMuFE3"
DEVELOPER_KEY = "Nyfm3hzIPWhifJdh31WgnKRu46RCVGjidPVUb8v7wi5MzomDwnqRnRyq9GuvIVEaxRYjnbvF-eULvU0MnT2vuw"

eliza_image_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"

package(
    Metadata(
        name="Eliza",
        image_url=eliza_image_url,
        color="f1a2b3",
        developer_uid=DEVELOPER_UID,
        description="I'm your confidante (...and therapist) (•̀ᴗ•́)و ̑̑",
        input_class=ElizaBot,
     ),
    requirements=["nltk"]
)


bot_uid = upload_and_deploy(
    "package.zip",
    uid=DEVELOPER_UID,
    key=DEVELOPER_KEY
)
wait_for_deployment(bot_uid)

bot_url = advertise_deployed_bot(bot_uid)
